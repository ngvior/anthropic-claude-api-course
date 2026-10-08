from anthropic import Anthropic
from dotenv import load_dotenv
import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
target_dir = os.path.abspath(
    os.path.join(current_dir, "..", "accessing_claude_with_the_api")
)
if target_dir not in sys.path:
    sys.path.append(target_dir)
import system_prompt as sp
import json

# messages = []
#
# prompt = f"""
# Please provide a solution to the following task:
# {task}
# """


def generate_dataset():
    prompt = """
Generate an evaluation dataset for a prompt evaluation. The dataset will be used to evaluate prompts that generate Python, JSON, or Regex specifically for AWS-related tasks. Generate an array of JSON objects, each representing task that requires Python, JSON, or a Regex to complete.

Example output:
```json
[
  \\{
    "task": "Description of task",
  \\},
  ...additional
]
```

* Focus on tasks that can be solved by writing a single Python function, a single JSON object, or a single regex
* Focus on tasks that do not require writing much code

Please generate 3 objects.
"""

    messages = []
    sp.add_message(messages, "user", prompt)
    sp.add_message(messages, "assistant", "```json")
    text = sp.chat(messages, stop_sequences=["```"])
    return json.loads(text)


if __name__ == "__main__":
    dataset = generate_dataset()
    print(dataset)
    with open(f"{current_dir}/dataset.json", "w") as f:
        json.dump(dataset, f, indent=2)
