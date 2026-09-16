from anthropic import Anthropic
from dotenv import load_dotenv
from typing import Literal
from system_prompt import add_message

load_dotenv()
client = Anthropic()

messages = []
model = "claude-haiku-4-5"

# def add_message(messages, role: Literal["user", "assistant"], text):
#     message = {"role": role, "content": text}
#     messages.append(message)

add_message(messages, "user", "Write a one sentence description of a fake database.")
print(messages)

# print("Basic Streaming Implementation")
# stream = client.messages.create(
#     max_tokens=1000,
#     model = model,
#     messages = messages,
#     stream = True
# )
# for event in stream:
#     print(event)

print("Simplified Text Streaming")
with client.messages.stream(
    max_tokens=1000,
    model = model,
    messages = messages
) as stream:
    for text in stream.text_stream:
        print(text, end="") # Send each stream chunk to the client for UX

    final_message = stream.get_final_message() # for storing in DB
