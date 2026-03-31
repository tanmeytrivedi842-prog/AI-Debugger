# webugmate-ai-debugger prompt
def build_prompt(code: str, error: str) -> str:
    return f"""
You are a senior software engineer.

Analyze the following code and error.

CODE:
{code}

ERROR:
{error}

Give:
1. Root cause
2. Fix
3. Improved code
4. Short explanation
"""