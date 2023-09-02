class CreateSubmission:
    def __init__(self, quiz_id: str):
        self.quiz_id = quiz_id
        self.answers = []

    def set_question_answer(self, question_id: int, choice_ids: list[int]):
        self.answers.append({
            'questionId': question_id,
            'choiceIds': choice_ids
        })