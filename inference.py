import asyncio
from env.environment import CustomerOpsEnv
from env.models import Action
from env.grader import grade_performance

MAX_STEPS = 5
MAX_TOTAL_REWARD = 5.0


async def main():
    env = await CustomerOpsEnv.from_docker_image("customer-ops-env")

    result = await env.reset("hard")
    obs = result.observation

    total_reward = 0

    for step in range(MAX_STEPS):

        ticket = sorted(
            obs.tickets,
            key=lambda t: (t.priority == "high", t.time_waiting),
            reverse=True
        )[0]

        action = Action(
            action_type="respond",
            ticket_id=ticket.id,
            message="Sorry for the inconvenience. We will resolve it quickly."
        )

        result = await env.step(action)

        print(f"Step {step+1}, Reward: {result.reward:.2f}")

        total_reward += result.reward
        obs = result.observation

        if result.done:
            break

    score = total_reward / MAX_TOTAL_REWARD
    score = min(max(score, 0.0), 1.0)

    grader_score = grade_performance(obs.tickets)

    print("\nFinal Score (0-1):", round(score, 2))
    print("Grader Score:", grader_score)

    await env.close()


if __name__ == "__main__":
    asyncio.run(main())