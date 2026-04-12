import os
import asyncio
from typing import List, Optional
from env import OpenEnvTaskSuite
from openenv_models import Action

# Optional OpenAI import (safe)
try:
    from openai import OpenAI
except:
    OpenAI = None

# ENV VARIABLES
API_BASE_URL = os.environ.get("API_BASE_URL", "https://api.openai.com/v1")
MODEL_NAME = os.environ.get("MODEL_NAME", "gpt-4o")
API_KEY = os.environ.get("OPENAI_API_KEY") or os.environ.get("HF_TOKEN")

MAX_STEPS = 5
TASK_NAME = "OpenEnvTaskSuite"
BENCHMARK = "openenv"

# ================= LOGGING =================

def log_start(task: str, env: str, model: str):
    print(f"[START] task={task} env={env} model={model}", flush=True)


def log_step(step: int, action: str, reward: float, done: bool, error: Optional[str]):
    error_val = error if error else "null"
    print(
        f"[STEP] step={step} action={action} reward={reward:.2f} done={str(done).lower()} error={error_val}",
        flush=True,
    )


def log_end(success: bool, steps: int, score: float, rewards: List[float]):
    rewards_str = ",".join(f"{r:.2f}" for r in rewards)
    print(
        f"[END] success={str(success).lower()} steps={steps} score={score:.3f} rewards={rewards_str}",
        flush=True,
    )

# ================= MAIN =================

async def main():
    # Initialize OpenAI ONLY if key exists (safe)
    client = None
    if API_KEY and OpenAI:
        try:
            client = OpenAI(base_url=API_BASE_URL, api_key=API_KEY)
        except Exception:
            client = None

    env = OpenEnvTaskSuite()

    rewards = []
    steps_taken = 0
    score = 0.0
    success = False

    log_start(task=TASK_NAME, env=BENCHMARK, model=MODEL_NAME)

    try:
        obs = await env.reset()

        for step in range(1, MAX_STEPS + 1):
            try:
                # 🔥 SMART ACTION SELECTION (UPDATED PART)
                if "email" in obs.state_description:
                    action = Action(action_type="classify", params={})
                elif "data" in obs.state_description:
                    action = Action(action_type="clean", params={})
                elif "meeting" in obs.state_description:
                    action = Action(action_type="schedule", params={})
                else:
                    action = Action(action_type="noop", params={})

                obs, reward = await env.step(action)

                rewards.append(reward.reward)

                log_step(
                    step,
                    action.action_type,
                    reward.reward,
                    reward.done,
                    None,
                )

                steps_taken += 1

                if reward.done:
                    success = True
                    score = reward.reward
                    break

            except Exception as step_err:
                log_step(step, "error", 0.0, True, str(step_err))
                break

    except Exception as e:
        print(f"[ERROR] {e}", flush=True)

    log_end(success, steps_taken, score, rewards)


if __name__ == "__main__":
    asyncio.run(main())