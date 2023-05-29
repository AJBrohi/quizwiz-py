from question_model import Question
from quiz_process import QuizProcessing
from question_data import question_data, category_list, difficulty_list

print("Categories Are - ")
for category in category_list:
    print(category.capitalize(), end="\n")
category_choice = input(
    "What category qustions you like to answer? - ").lower()

print("\n")

print("Difficulties Are - ")
for difficulty in difficulty_list:
    print(difficulty.capitalize(), end="\n")
difficulty_choice = input(
    "What difficulty qustions you like to answer? - ").lower()

question_bank = []

for question in question_data:
    if category_choice in question["category"] and difficulty_choice in question["difficulty"]:
        question_text = question["question"]
        question_answer = question["correct_answer"]
        new_question = Question(question_text, question_answer)
        question_bank.append(new_question)

if question_bank:
    quiz = QuizProcessing(question_bank)
    # clear
    print(f"Category: {category_choice.capitalize()}")
    print(f"Diffuculty: {difficulty_choice.capitalize()}")

    while quiz.questions_remaining():
        quiz.next_question()

    quiz.print_answers()
else:
    print("Wrong Choice. Try Again!!")
