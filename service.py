# webugmate-ai-debugger service
import os
from dotenv import load_dotenv
from openai import OpenAI
from app.prompt import build_prompt

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def analyze_code(code: str, error: str):
    prompt = build_prompt(code, error)

    response = client.chat.completions.create(
        model="gpt-4.1-mini",  # fast & cheap
        messages=[
            {"role": "system", "content": "You are a helpful debugging assistant."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.3
    )

    return response.choices[0].message.content