#fastapi application and setup

# en este archivo se levanta una interfaz de programacion de 
# aplicaciones

from fastapi import FastAPI

from services import sum, infer_prompt

app = FastAPI()


@app.get("/health_check")
def health_check():
    """
    Returns status of the server
    """
    return {"status": "online"}


@app.get("/sum")
def get_sum(num1: int, num2: int) -> dict:
    """
    Returns the sum of two numbers
    Args:
        num1: int to sum
        num1: int to sum
    Returns:
        Dict containing the result of the sum
    """
    result = sum(num1, num2)
    return {"result": result}


@app.get("/call_llm")
def get_llm_response(prompt: str) -> dict:
    result = infer_prompt(prompt)
    return {"result": result}