def zero_shot_prompt(task, context):
    return f"""
Task: {task}
Context: {context}
Provide an accurate, clear and useful response.
"""
def few_shot_prompt(task, examples, new_input):
    return f"""
Task: {task}
Examples:
{examples}
Now perform the same task for:
{new_input}
Answer:
"""
def role_based_prompt(role, task, audience, constraints):
    return f"""
Act as: {role}
Task: {task}
Target audience: {audience}
Constraints: {constraints}
Provide a clear and relevant response.
"""
def json_prompt(task, data):
    return f"""
Task: {task}
Input data:
{data}
Return the result in valid JSON format only.
Do not include Markdown code fences.
"""
