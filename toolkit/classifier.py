def build_classification_prompt(text):
    return f"""
You are an expert text classification assistant.
Analyze the following text and classify its category.
Explain the reason for your classification.
TEXT:
{text}
CLASSIFICATION:
"""
