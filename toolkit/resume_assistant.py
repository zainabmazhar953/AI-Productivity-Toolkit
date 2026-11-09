def build_resume_prompt(skills, role):
    return f"""
You are an expert resume writing assistant.
Candidate skills: {skills}
Target job role: {role}
Create professional resume content tailored to this job.
Include:
1. Professional summary
2. Technical skills
3. Relevant project suggestions
4. Experience section guidance
5. Keywords suitable for ATS screening
RESUME:
"""
