from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
from env.environment import CustomerOpsEnv
from env.models import Action
import uvicorn

app = FastAPI()

env = CustomerOpsEnv()


class ResetRequest(BaseModel):
    difficulty: Optional[str] = "hard"


class StepRequest(BaseModel):
    action_type: str
    ticket_id: int
    message: str


@app.post("/reset")
async def reset(req: ResetRequest = ResetRequest()):
    result = await env.reset(req.difficulty)

    return {
        "observation": result.observation.dict(),
        "reward": result.reward,
        "done": result.done,
    }


@app.post("/step")
async def step(req: StepRequest):
    action = Action(
        action_type=req.action_type,
        ticket_id=req.ticket_id,
        message=req.message
    )

    result = await env.step(action)

    return {
        "observation": result.observation.dict(),
        "reward": result.reward,
        "done": result.done,
    }


# ✅ REQUIRED main() FUNCTION
def main():
    uvicorn.run("server.app:app", host="0.0.0.0", port=7860)


# ✅ REQUIRED ENTRY POINT
if __name__ == "__main__":
    main()