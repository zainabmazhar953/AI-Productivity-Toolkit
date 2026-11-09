
def evaluate_prompt(prompt):

    prompt = prompt.lower()

    checks = {
        "Clear instructions": any(
            word in prompt for word in
            ["task", "summarize", "classify", "generate", "write"]
        ),

        "Context provided": any(
            word in prompt for word in
            ["context", "input", "text", "data"]
        ),

        "Role defined": any(
            word in prompt for word in
            ["act as", "role"]
        ),

        "Output format": any(
            word in prompt for word in
            ["format", "return", "json", "output"]
        ),

        "Constraints included": any(
            word in prompt for word in
            ["do not", "constraints", "only", "accurate"]
        )
    }

    score = sum(checks.values())

    print("\nPROMPT EVALUATION")
    print("-" * 40)

    for name, status in checks.items():
        print(name, ":", "PASS" if status else "IMPROVE")

    print("\nPROMPT QUALITY SCORE:", score, "/5")

    if score == 5:
        print("Excellent prompt structure!")
    else:
        print("Improve the missing prompt elements.")

    return score
