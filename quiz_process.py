class QuizProcessing:
    def __init__(self, ques_list):
        self.question_number = 0
        self.score = 0
        self.question_list = ques_list

    def questions_remaining(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        ques = self.question_list[self.question_number]
        self.question_number += 1
        ans = input(f"Q.{self.question_number}: {ques.text} (True/False) - ")
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
