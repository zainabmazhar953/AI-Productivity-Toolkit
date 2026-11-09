def build_summary_prompt(text):
    return f"""
You are an expert text summarizer.
Summarize the following text clearly.
Include the main points and important information.
Avoid repetition.
TEXT:
{text}
SUMMARY:
"""
