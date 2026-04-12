from openenv_models import Observation, Action, Reward
from tasks import email_triage, data_cleaning, meeting_scheduling

class OpenEnvTaskSuite:
    def __init__(self):
        self.step_count = 0
        self.current_task = None
        self.tasks = ["email_triage", "data_cleaning", "meeting_scheduling"]
        self.task_index = 0
        self.action_history = []

    async def reset(self):
        self.step_count = 0
        self.action_history = []
        self.current_task = self.tasks[self.task_index]

        return Observation(
            state_description=f"Task: {self.current_task}",
            data={"task": self.current_task}
        )

    async def step(self, action: Action):
        self.step_count += 1
        self.action_history.append(action.action_type)

        # -------- BASE REWARD -------- #
        reward = 0.05

        if self.current_task == "email_triage" and action.action_type == "classify":
            reward = 0.2
        elif self.current_task == "data_cleaning" and action.action_type == "clean":
            reward = 0.2
        elif self.current_task == "meeting_scheduling" and action.action_type == "schedule":
            reward = 0.2

        done = self.step_count >= 5

        # -------- GRADER SCORE -------- #
        if self.current_task == "email_triage":
            score = email_triage.grader(self.action_history)
        elif self.current_task == "data_cleaning":
            score = data_cleaning.grader(self.action_history)
        else:
            score = meeting_scheduling.grader(self.action_history)

        # Switch task after done
        if done:
            self.task_index = (self.task_index + 1) % len(self.tasks)

        return (
            Observation(
                state_description=f"{self.current_task} step {self.step_count}",
                data={"task": self.current_task}
            ),
            Reward(reward=score, done=done)
        )

    async def state(self):
        return Observation(
            state_description=f"{self.current_task} step {self.step_count}",
            data={"task": self.current_task}
        )