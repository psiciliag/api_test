# a client that asks for a request to our server

# hola pablo, quiero saber cuanto es 2 + 4
# te hago una solicitud a tu ordenador con los parametros 2 y 4

import requests

URL = "http://127.0.0.1:8000"

def call_and_print_response(url: str, payload: dict|None = None):
    response = requests.get(url, payload)
    print(response)
    if response.status_code == 200:
        print(response.content)


# get elordenardordepablo:8080/health_check

def call_health_check():
    """
    Function that calls /health_check on the specified URL
    Prints the result if the status code is "200 OK"
    """
    health_check_url = URL + "/health_check"
    call_and_print_response(health_check_url)


# get elordenardordepablo:8080/suma

def call_sum(num1: int, num2: int):
    """
    Function that calls /sum on the specified URL
    Prints the result if the status code is "200 OK"
    """
    sum_url = URL + "/sum"
    params = {
        "num1": num1,
        "num2": num2
    }
    call_and_print_response(sum_url, params)
        

# get elordenardordepablo:8080/call_llm

def call_llm(prompt: str):
    llm_url = URL + "/call_llm"
    params = {
        "prompt": prompt
    }
    call_and_print_response(llm_url, params)


if __name__ == "__main__":
    prompt = input("¿Qué quieres decirle al LLM?")
    call_llm(prompt)
