from pydantic import BaseModel
from typing import List, Optional


class Ticket(BaseModel):
    id: str
    issue: str
    priority: str  # low, medium, high
    customer_tone: str  # calm, neutral, angry
    time_waiting: int
    resolved: bool = False


class Resource(BaseModel):
    agents_available: int


class Observation(BaseModel):
    tickets: List[Ticket]
    resources: Resource
    message: Optional[str] = None


class Action(BaseModel):
    action_type: str  # "respond" or "prioritize"
    ticket_id: str
    message: Optional[str] = None


class StepResult(BaseModel):
    observation: Observation
    reward: float
    done: bool