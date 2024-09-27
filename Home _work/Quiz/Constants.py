class Team:
    def __init__(self, team_name):
        self.team_name = team_name
        self.points = 0
        self.answers = {}

    def give_answer(self, question, answer):
        self.answers[question.question_text] = answer
        if answer.lower() == question.correct_answer.lower():
            self.points += 1


class Question:
    def __init__(self, correct_answer, question_text):
        self.correct_answer = correct_answer
        self.question_text = question_text



















