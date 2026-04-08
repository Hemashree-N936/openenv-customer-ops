# inference.py
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow Hugging Face to call endpoints
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class ResetRequest(BaseModel):
    pass

@app.post("/reset")
async def reset(req: ResetRequest):
    return {
        "observation": {"echoed_message": "Hello, World!"},
        "reward": 0.0,
        "done": False
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=7860)