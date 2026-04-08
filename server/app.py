from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
from env.environment import CustomerOpsEnv
from env.models import Action
import uvicorn

app = FastAPI()

env = CustomerOpsEnv()


# ✅ RESET REQUEST
class ResetRequest(BaseModel):
    difficulty: Optional[str] = "hard"


# ✅ STEP REQUEST (validator expects int)
class StepRequest(BaseModel):
    action_type: str
    ticket_id: int   # MUST be int for validator
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
    # 🔥 FIX: convert int → "T1"
    ticket_id_str = f"T{req.ticket_id}"

    action = Action(
        action_type=req.action_type,
        ticket_id=ticket_id_str,   # env expects string
        message=req.message
    )

    result = await env.step(action)

    return {
        "observation": result.observation.dict(),
        "reward": result.reward,
        "done": result.done,
    }


# ✅ REQUIRED main() for OpenEnv
def main():
    uvicorn.run("server.app:app", host="0.0.0.0", port=7860)


# ✅ REQUIRED entrypoint
if __name__ == "__main__":
    main()