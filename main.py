# webugmate-ai-debugger app main
from fastapi import FastAPI
from app.routes import router

app = FastAPI(title="Webugmate AI Debugger")

app.include_router(router)

@app.get("/")
def root():
    return {"message": "AI Debugging Assistant Running 🚀"}