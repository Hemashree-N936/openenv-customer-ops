from pydantic import BaseModel
from typing import Optional, Dict, Any

class Observation(BaseModel):
    state_description: str
    data: Optional[Dict[str, Any]] = None

class Action(BaseModel):
    action_type: str
    params: Dict[str, Any]

class Reward(BaseModel):
    reward: float
    done: bool