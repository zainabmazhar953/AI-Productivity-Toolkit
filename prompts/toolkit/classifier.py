
def build_classification_prompt(text):
    return f"""
Act as a text classification assistant.

TEXT:
{text}

TASK:
Classify the sentiment into one category:
- Positive
- Negative
- Neutral

OUTPUT:
Category:
Reason:

Explain your classification in one sentence.
"""
