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
from statistics import mean


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

    # Grade the output
    model_grade = grade_by_model(test_case, output)
    score = model_grade["score"]
    reasoning = model_grade["reasoning"]

    return {
        "output": output,
        "test_case": test_case,
        "score": score,
        "reasoning": reasoning,
    }


def run_eval(dataset):
    """Loads the dataset and runs run_test_case with each case"""
    results = []

    for test_case in dataset:
        result = run_test_case(test_case)
        results.append(result)

    average_score = mean([result["score"] for result in results])
    print(f"Average score: {average_score}")

    return results


def grade_by_model(test_case, output):
    # Create evaluation prompt
    eval_prompt = f"""
    You are an expert code reviewer. Evaluate this AI-generated solution.
    
    Task: {test_case}
    Solution: {output}
    
    Provide your evaluation as a structured JSON object with:
    - "strengths": An array of 1-3 key strengths
    - "weaknesses": An array of 1-3 key areas for improvement  
    - "reasoning": A concise explanation of your assessment
    - "score": A number between 1-10
    """

    messages = []
    sp.add_message(messages, "user", eval_prompt)
    sp.add_message(messages, "assistant", "```json")
    eval_text = sp.chat(messages, stop_sequences=["```"])
    return json.loads(eval_text)


if __name__ == "__main__":
    with open("prompt_evaluation/dataset.json", "r") as f:
        dataset = json.load(f)

    results = run_eval(dataset)

    print(json.dumps(results, indent=2))
