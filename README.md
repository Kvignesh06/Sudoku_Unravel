# Sudoku_Unravel
**A 9x9 sudoku solver that gives all possible combinations of answers using a backtracking algorithm for the given unsolved puzzle.**



# model_connector.py
import requests

LLM_SERVER_URL = "http://<your-llm-ip>:<port>/generate"  # 👈 Replace this

def query_model(prompt: str) -> str:
    try:
        response = requests.post(LLM_SERVER_URL, json={"prompt": prompt}, timeout=10)
        response.raise_for_status()
        return response.json().get("response", "No response key found")
    except Exception as e:
        return f"Model error: {str(e)}"
