# webugmate-ai-debugger utils
import datetime

def log_request(code, error):
    with open("logs.txt", "a") as f:
        f.write(f"{datetime.datetime.now()}\n")
        f.write(f"CODE:\n{code}\n")
        f.write(f"ERROR:\n{error}\n\n")