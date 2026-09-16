# Lessons 5 & 6

from anthropic import Anthropic
from dotenv import load_dotenv
from typing import Literal

load_dotenv()

client = Anthropic()
model = "claude-haiku-4-5"
messages = []

Roles = Literal["user", "assistant"]

def add_message(messages, role: Roles, text):
    message = {"role": role, "content": text}
    messages.append(message)

def chat(messages, system_prompt=None, temperature=1.0):
    params = {
        "model": model,
        "max_tokens": 1000,
        "messages": messages,
        "extra_body": { "temperature": temperature } 
    }
    if system_prompt:
        params["system"] = system_prompt

    message = client.messages.create(**params)
    return message.content[0].text

inputs = {
    "system_prompt": input("Enter system prompt (or leave blank):\n"),
    "temperature": input("Enter the model temperature (or leave blank):\n")
}
filtered_params = {}
for key, val in inputs.items():
    if val:
        if key == "temperature":
            filtered_params[key] = float(val)
        else:
            filtered_params[key] = val
print(filtered_params)
i = -1
while i != 0:
    prompt = input("prompt (leave blank to quit):\n")
    if prompt:
        add_message(messages, "user", prompt)
        response = chat(messages, **filtered_params)
        add_message(messages, "assistant", response)
        print("response:\n" + response)
        print("--------------------")
    else:
        i = 0
        print("Bye!")

