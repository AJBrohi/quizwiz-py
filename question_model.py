class Question:
    def __init__(self, q_text, q_answer):
        """
        Represents a question object with its text and answer.

        Args:
        q_text (str): The text of the question.
        q_answer (bool): The answer to the question (True for 'yes' or False for 'no').
        """
        self.text = q_text
        self.answer = q_answer
