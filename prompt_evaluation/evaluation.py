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


def run_prompt(test_case):
    """Merges the prompt and test case input, then returns the result"""
    prompt = f"""
Please solve the following task:

{test_case["task"]}
"""

    messages = []
    sp.add_message(messages, "user", prompt)
    output = sp.chat(messages)
    return output


def run_test_case(test_case):
    """Calls run_prompt, then grades the result"""
    output = run_prompt(test_case)

    # TODO - Grading
    score = 10

    return {"output": output, "test_case": test_case, "score": score}


def run_eval(dataset):
    """Loads the dataset and runs run_test_case with each case"""
    results = []

    for test_case in dataset:
        result = run_test_case(test_case)
        results.append(result)

    return results


if __name__ == "__main__":
    with open("prompt_evaluation/dataset.json", "r") as f:
        dataset = json.load(f)

    results = run_eval(dataset)

    print(json.dumps(results, indent=2))
