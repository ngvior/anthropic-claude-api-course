import json

from anthropic import Anthropic
from dotenv import load_dotenv

import system_prompt as sp

load_dotenv()
client = Anthropic()

messages = []

sp.add_message(messages, "user", "Generate a very short event bridge rule as json")
sp.add_message(messages, "assistant", "```json")
response = sp.chat(messages, stop_sequences=["```"])
print(response)

clean_json = json.loads(response.strip())
print(clean_json)
