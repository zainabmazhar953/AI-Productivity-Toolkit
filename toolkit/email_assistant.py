def build_email_prompt(purpose, recipient, tone):
    return f"""
You are a professional email writing assistant.
Email purpose: {purpose}
Recipient: {recipient}
Tone: {tone}
Write a complete, professional email with:
- Appropriate subject
- Greeting
- Clear body
- Professional closing
EMAIL:
"""
