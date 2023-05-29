class QuizProcessing:
    def __init__(self, ques_list):
        """
        Represents a quiz processing object.

        Args:
        ques_list (list): A list of Question objects representing the quiz questions.
        """
        self.question_number = 0
        self.score = 0
        self.question_list = ques_list
        self.answers_list = []

    def questions_remaining(self):
        """
        Checks if there are any questions remaining in the quiz.

        Returns:
        bool: True if there are questions remaining, False otherwise.
        """
        return self.question_number < len(self.question_list)

    def next_question(self):
        """
        Displays the next question, prompts the user for an answer, and checks if the answer is correct.
        Updates the score and answers list accordingly.
        """
        ques = self.question_list[self.question_number]
        self.question_number += 1
        ans = input(f"Q.{self.question_number}: {ques.text} (True/False) - ")
        self.answers_list.append(ans)
        self.check_answer(ans, ques.answer)

    def check_answer(self, answer, q_answer):
        """
        Checks if the provided answer matches the correct answer.
        Updates the score based on the correctness of the answer.

        Args:
        answer (str): The user's answer to the question.
        q_answer (bool): The correct answer to the question.
        """
        if answer.lower() == q_answer.lower():
            print("Your answer is correct.")
            self.score += 1
        else:
            print("Your answer is wrong.")
            print(f"Correct answer is: {q_answer}")

        print(
            f"Your current score is: {self.score}/{self.question_number}\n")

    def print_answers(self):
        """
        Prints the user's answers along with the correct answers for all the questions in the quiz, as well as the final score.
        """
        print("You've completed the quiz.")

        for i in range(len(self.question_list)):
            question = self.question_list[i]
            print(f"""For Q{i+1}.
Your answer was - {self.answers_list[i]}
Correct answer was - {question.answer}""")

        print()
        print(f"Your final score is: {self.score}/{self.question_number}")
        print("Thank you for taking the quiz chellange.")
