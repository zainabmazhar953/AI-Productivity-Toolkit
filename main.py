
from prompts.prompt_templates import (
    zero_shot_prompt,
    few_shot_prompt,
    role_based_prompt,
    json_prompt
)

from toolkit.summarizer import build_summary_prompt
from toolkit.classifier import build_classification_prompt
from toolkit.email_assistant import build_email_prompt
from toolkit.resume_assistant import build_resume_prompt
from toolkit.prompt_evaluator import evaluate_prompt


def show_menu():

    print("\n" + "=" * 55)
    print("          AI PRODUCTIVITY TOOLKIT")
    print("          PROMPT ENGINEERING SYSTEM")
    print("=" * 55)

    print("""
1. Zero-shot Prompting
2. Few-shot Prompting
3. Role-based Prompting
4. Structured JSON Prompt
5. Text Summarization
6. Text Classification
7. Email Assistant
8. Resume Assistant
9. Prompt Evaluation
0. Exit
""")


def get_input(message):
    return input(message).strip()


def save_prompt(prompt):

    answer = get_input("\nSave generated prompt? (yes/no): ")

    if answer.lower() == "yes":

        with open(
            "outputs/generated_prompts.txt",
            "a",
            encoding="utf-8"
        ) as file:

            file.write(prompt + "\n")
            file.write("=" * 50 + "\n")

        print("Prompt saved successfully!")


def main():

    while True:

        show_menu()

        choice = get_input("Enter your choice: ")

        if choice == "1":

            task = get_input("Enter task: ")
            context = get_input("Enter context: ")

            result = zero_shot_prompt(task, context)

        elif choice == "2":

            task = get_input("Enter task: ")
            examples = get_input("Enter examples: ")
            new_input = get_input("Enter new input: ")

            result = few_shot_prompt(
                task, examples, new_input
            )

        elif choice == "3":

            role = get_input("Enter AI role: ")
            task = get_input("Enter task: ")
            audience = get_input("Enter audience: ")
            constraints = get_input("Enter constraints: ")

            result = role_based_prompt(
                role, task, audience, constraints
            )

        elif choice == "4":

            task = get_input("Enter task: ")
            data = get_input("Enter input data: ")

            result = json_prompt(task, data)

        elif choice == "5":

            text = get_input("Enter text: ")

            result = build_summary_prompt(text)

        elif choice == "6":

            text = get_input("Enter text: ")

            result = build_classification_prompt(text)

        elif choice == "7":

            purpose = get_input("Enter email purpose: ")
            recipient = get_input("Enter recipient: ")
            tone = get_input("Enter tone: ")

            result = build_email_prompt(
                purpose, recipient, tone
            )

        elif choice == "8":

            skills = get_input("Enter skills: ")
            role = get_input("Enter target job: ")

            result = build_resume_prompt(skills, role)

        elif choice == "9":

            prompt = get_input("Paste your prompt: ")

            evaluate_prompt(prompt)

            input("\nPress Enter to continue...")
            continue

        elif choice == "0":

            print("Thank you for using AI Productivity Toolkit!")
            break

        else:

            print("Invalid choice! Try again.")
            input("Press Enter...")
            continue

        print("\nGENERATED PROMPT")
        print("-" * 50)
        print(result)

        save_prompt(result)

        input("\nPress Enter to continue...")


if __name__ == "__main__":
    main()
