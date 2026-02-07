# logica de los servicios que hace la app

def sum(num1: int, num2: int) -> int:
    """
    Function that sums two numbers
    Args:
        num1: number to sum 1
        num2: number to sum 2
    Returns:
        int: sum of the two numbers
    """
    return num1 + num2

def infer_prompt(prompt: str) -> str:
    """
    Function that uses an LLM to infer
    Args:
        prompt: str the user sends
    Returns:
        The response of the LLM
    """
    return "Soy una IA y entiendo lo que me has dicho"