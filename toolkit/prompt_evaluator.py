def evaluate_prompt(prompt):
    if not prompt.strip():
        print("Prompt cannot be empty!")
        return 0
    checks = {
        "Clear instructions": len(prompt.split()) >= 5,
        "Context provided": any(x in prompt.lower() for x in ["context", "background", "role"]),
        "Specific task": any(x in prompt.lower() for x in ["summarize", "explain", "write", "analyze", "create"]),
        "Output guidance": any(x in prompt.lower() for x in ["format", "include", "list", "json", "output"]),
        "Sufficient detail": len(prompt.split()) >= 15
    }
    score = sum(checks.values())
    print("\n========== PROMPT EVALUATION ==========")
    for name, passed in checks.items():
        print(f"{name}: {'PASS' if passed else 'NEEDS IMPROVEMENT'}")
    print(f"\nPrompt Quality Score: {score}/5")
    if score >= 4:
        print("Rating: Excellent!")
    elif score >= 3:
        print("Rating: Good!")
    else:
        print("Rating: Needs Improvement")
    return score
