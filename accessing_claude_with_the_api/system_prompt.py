# Lessons 5 & 6

from typing import Literal

from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()

client = Anthropic()
model = "claude-haiku-4-5"
messages = []

Roles = Literal["user", "assistant"]


def add_message(messages, role: Roles, text):
    message = {"role": role, "content": text}
    messages.append(message)


def chat(messages, system_prompt=None, temperature=1.0, stop_sequences=None):
    params = {
        "model": model,
        "max_tokens": 1000,
        "messages": messages,
        "extra_body": {"temperature": temperature},
    }
    if system_prompt:
        params["system"] = system_prompt
    if stop_sequences:
        params["stop_sequences"] = stop_sequences
    message = client.messages.create(**params)
    return message.content[0].text


if __name__ == "__main__":
    inputs = {
        "system_prompt": input("Enter system prompt (or leave blank):\n"),
        "temperature": input("Enter the model temperature (or leave blank):\n"),
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
