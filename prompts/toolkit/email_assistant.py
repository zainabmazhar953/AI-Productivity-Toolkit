
def build_email_prompt(purpose, recipient, tone):
    return f"""
Act as a professional email writing assistant.

PURPOSE:
{purpose}

RECIPIENT:
{recipient}

TONE:
{tone}

Generate an email with:
1. Suitable subject line.
2. Professional greeting.
3. Clear email body.
4. Appropriate closing.

Use correct grammar and do not invent details.
"""
