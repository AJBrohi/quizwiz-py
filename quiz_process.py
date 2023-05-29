class QuizProcessing:
    def __init__(self, ques_list):
        self.question_number = 0
        self.score = 0
        self.question_list = ques_list
        self.answers_list = []

    def questions_remaining(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        ques = self.question_list[self.question_number]
        self.question_number += 1
        ans = input(f"Q.{self.question_number}: {ques.text} (True/False) - ")
        self.answers_list.append(ans)
        self.check_answer(ans, ques.answer)

    def check_answer(self, answer, q_answer):
        if answer.lower() == q_answer.lower():
            print("Your answer is correct.")
            self.score += 1
        else:
            print("Your answer is wrong.")
            print(f"Correct answer is: {q_answer}")

        print(
            f"Your current score is: {self.score}/{self.question_number}\n")

    def print_answers(self):
        print("You've completed the quiz.")

        for i in range(len(self.question_list)):
            question = self.question_list[i]
            print(f"""For Q{i+1}.
Your answer was - {self.answers_list[i]}
Correct answer was - {question.answer}""")

        print()
        print(f"Your final score is: {self.score}/{self.question_number}")
        print("Thank you for taking the quiz chellange.")
