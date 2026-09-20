"""Python quiz application.



Sample:

    Q1. Which keyword defines a function in Python?

      a) func  b) def  c) define  d) lambda

    Your answer: b -> Correct!

    Final score: 4/5 (80.00%)

"""



QUESTIONS = [

    {"question": "Which keyword defines a function in Python?",

     "options": {"a": "func", "b": "def", "c": "define", "d": "lambda"}, "answer": "b"},

    {"question": "What is the output of len([1, 2, 3])?",

     "options": {"a": "2", "b": "3", "c": "4", "d": "Error"}, "answer": "b"},

    {"question": "Which data type is immutable?",

     "options": {"a": "list", "b": "dict", "c": "tuple", "d": "set"}, "answer": "c"},

    {"question": "What does 10 // 3 return?",

     "options": {"a": "3.33", "b": "3", "c": "4", "d": "1"}, "answer": "b"},

    {"question": "Which loop runs while a condition is True?",

     "options": {"a": "for", "b": "while", "c": "do-while", "d": "foreach"}, "answer": "b"},

]





def ask_question(number, item):

    """Show one question, read a valid answer, return True if correct."""

    print(f"\nQ{number}. {item['question']}")

    for key, text in item["options"].items():

        print(f"   {key}) {text}")



    while True:

        answer = input("Your answer (a/b/c/d): ").strip().lower()

        if answer in item["options"]:

            break

        print("Please enter a, b, c or d.")



    if answer == item["answer"]:

        print("Correct!")

        return True

    print(f"Wrong. Correct answer: {item['answer']}) {item['options'][item['answer']]}")

    return False





def calculate_percentage(score, total):

    """Return score as a percentage."""

    return score / total * 100





def main():

    score = 0

    number = 1

    for item in QUESTIONS:

        if ask_question(number, item):

            score += 1

        number += 1



    percentage = calculate_percentage(score, len(QUESTIONS))

    print("\n=== Quiz Finished ===")

    print(f"Score: {score}/{len(QUESTIONS)}")

    print(f"Percentage: {percentage:.2f}%")





if __name__ == "__main__":

    main()
