
def build_summary_prompt(text):
    return f"""
Act as a professional summarization assistant.

TEXT:
{text}

TASK:
Summarize the given text.

REQUIREMENTS:
1. Identify the main idea.
2. Extract important points.
3. Remove unnecessary details.
4. Use simple English.
5. Keep the summary under 100 words.
6. Do not add unsupported facts.
"""
