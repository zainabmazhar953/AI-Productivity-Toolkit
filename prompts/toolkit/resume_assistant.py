
def build_resume_prompt(skills, target_role):
    return f"""
Act as an expert resume assistant.

CANDIDATE SKILLS:
{skills}

TARGET ROLE:
{target_role}

Generate:
1. Professional resume summary.
2. Relevant technical skills.
3. Suggested project descriptions.
4. Important job-related keywords.

IMPORTANT:
- Do not invent qualifications.
- Do not invent work experience.
- Use only the information provided.
"""
