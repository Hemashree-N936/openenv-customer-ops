import asyncio
from .models import Observation, Action, StepResult
from .tasks import easy_task, medium_task, hard_task
from .reward import calculate_reward


class CustomerOpsEnv:

    def __init__(self):
        self.state = None
        self.done = False
        self.step_count = 0

    @classmethod
    async def from_docker_image(cls, image_name: str):
        # For now, just return instance (OpenEnv compatibility placeholder)
        return cls()

    async def reset(self, difficulty="hard"):
        await asyncio.sleep(0)  # simulate async

        if difficulty == "easy":
            self.state = easy_task()
        elif difficulty == "medium":
            self.state = medium_task()
        else:
            self.state = hard_task()

        self.done = False
        self.step_count = 0

        return StepResult(
            observation=Observation(
                tickets=self.state["tickets"],
                resources=self.state["resources"]
            ),
            reward=0.0,
            done=False
        )

    async def step(self, action: Action):
        await asyncio.sleep(0)

        self.step_count += 1
        reward = 0.0

        for ticket in self.state["tickets"]:
            if ticket.id == action.ticket_id:
                reward = calculate_reward(ticket, action, self.step_count)

        if all(t.resolved for t in self.state["tickets"]):
            self.done = True

        return StepResult(
            observation=Observation(
                tickets=self.state["tickets"],
                resources=self.state["resources"]
            ),
            reward=reward,
            done=self.done
        )

    async def close(self):
        await asyncio.sleep(0)