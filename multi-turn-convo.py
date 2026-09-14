from typing import Literal
from dotenv import load_dotenv
load_dotenv()

from anthropic import Anthropic

client = Anthropic()
model = "claude-haiku-4-5"
messages = []

Roles = Literal["user", "assistant"]

def add_message(messages, role: Roles, text):
    message = {"role": role, "content": text}
    messages.append(message)

def chat(messages):
    response = client.messages.create(
        model = model,
        max_tokens = 1000,
        messages = messages
    )
    return response.content[0].text

def line():
    print("--------------------")

keep_going = 1
while keep_going == 1:
    prompt = input("prompt ('0' to quit):\n")
    line()
    if prompt != '0':
        add_message(messages, "user", prompt)
        response = chat(messages)
        add_message(messages, "assistant", response)
        print("response:\n" + response)
        line()
    else: 
        keep_going = 0
        print("Bye!")

