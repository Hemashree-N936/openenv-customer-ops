from fastapi import FastAPI
from pydantic import BaseModel
from env.environment import CustomerOpsEnv
from env.models import Action

app = FastAPI()

env = CustomerOpsEnv()


class ResetRequest(BaseModel):
    difficulty: str = "hard"


class StepRequest(BaseModel):
    action_type: str
    ticket_id: str   # IMPORTANT: string, not int
    message: str


@app.post("/reset")
async def reset(req: ResetRequest):
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


@app.get("/")
def home():
    return {"status": "running"}