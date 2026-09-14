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

def chat(messages, system=None):
    params = {
        "model": model,
        "max_tokens": 1000,
        "messages": messages
    }
    if system:
        params["system"] = system
    message = client.messages.create(**params)
    return message.content[0].text

system_prompt = input("Enter system prompt (or leave blank):\n")
i = -1
while i != 0:
    prompt = input("prompt ('0' to quit):\n")
    if prompt != '0':
        add_message(messages, "user", prompt)
        response = chat(messages, system=system_prompt if system_prompt else None)
        add_message(messages, "assistant", response)
        print("response:\n" + response)
        print("--------------------")
    else:
        i = 0
        print("Bye!")
