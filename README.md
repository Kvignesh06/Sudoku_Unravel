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
    except Exception as e 
        return f"Model error: {str(e)}"


# memory.py
class ChatMemory:
    def __init__(self):
        self.history = []

    def add(self, user_msg: str, bot_msg: str):
        self.history.append((user_msg, bot_msg))

    def get_prompt(self, new_input: str) -> str:
        prompt = ""
        for user, bot in self.history:
            prompt += f"User: {user}\nBot: {bot}\n"
        prompt += f"User: {new_input}\nBot:"
        return prompt



        # agent.py
from flask import Flask, request, jsonify
from memory.py import ChatMemory
from model_connector import query_model

app = Flask(__name__)
memory = ChatMemory()

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_input = data.get("input", "")
    
    if not user_input:
        return jsonify({"error": "No input provided"}), 400

    prompt = memory.get_prompt(user_input)
    bot_output = query_model(prompt)
    memory.add(user_input, bot_output)

    return jsonify({"response": bot_output})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5050)
