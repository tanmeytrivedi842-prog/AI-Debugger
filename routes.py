# webugmate-ai-debugger routes
from fastapi import APIRouter
from pydantic import BaseModel
from app.service import analyze_code

router = APIRouter()

class DebugRequest(BaseModel):
    code: str
    error: str

@router.post("/debug")
async def debug_code(request: DebugRequest):
    result = analyze_code(request.code, request.error)
    return {"result": result}