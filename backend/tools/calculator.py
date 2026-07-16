import re

def calculator(expression: str):
    try:
        cleaned = re.sub(r"[^0-9+\-*/(). ]", "", expression)
        result = eval(cleaned)
        return f"Result: {result}"
    except Exception:
        return "Invalid expression."