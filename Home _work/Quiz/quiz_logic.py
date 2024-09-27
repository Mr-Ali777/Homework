from Constants import Team, Question
import random


class Quiz:
    def __init__(self, questions, teams):
        self.questions = questions
        self.teams = teams
        self.used_questions = []

    def quiz_start(self):
        for team in self.teams:
            print(f'Команда "{team.team_name}", ваш ход!')
            ramdom_question = self.choose_question()
            if ramdom_question:
                print(ramdom_question.question_text)
                answer = input("Введите ответ вашей команды: ")
                team.give_answer(ramdom_question, answer)

    def choose_question(self):
        remain_question = [q for q in self.questions if q not in self.used_questions]
        if remain_question:
            q = random.choice(remain_question)
            self.used_questions.append(q)
            return q
        return None

    def show_result(self):
        print("Результаты викторины: ")
        for team in self.teams:
            print(f'Команда "{team.team_name}" заработала {team.points} баллов.')
            for question, answer in team.answers.items():
                print(f'Вопрос: {question}, Ответ: {answer}')






