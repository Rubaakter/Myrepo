import requests

QUIZ_URL = "https://bjornkjellgren.se/quiz/v2/questions"


class Answer:
    # Implementera klassen Answer
    # Vilka attribut skall den ha?
    # Vilka metoder behöver vi?
    answer: str
    correct: bool

    def __init__(self, answer, correct):
        self.answer = answer
        self.correct = correct

    def __str__(self):
        return self.answer


class Question:
    id: int
    prompt: str
    times_asked: int
    times_correct: int
    answers: list[Answer]

    def __init__(self, id_, prompt, times_asked, times_correct, answers: list[Answer]):
        self.id = int(id_)
        self.prompt = prompt
        self.times_asked = int(times_asked)
        self.times_correct = int(times_correct)
        self.answers = answers

    def percent_correct(self) -> str:
        return f"{self.times_correct / self.times_asked:.0%} har svarat rätt"


def get_questions() -> list[Question]:
    response = requests.get(QUIZ_URL).json()
    res = []
    for q in response['questions']:
        res.append(parse_question(q))
    return res


def parse_answers(answers) -> list[Answer]:
    res = []
    for a in answers:
        res.append(Answer(a['answer'], a['correct']))
    return res


def parse_question(q) -> Question:
    return Question(q['id'], q['prompt'], q['times_asked'], q['times_correct'], parse_answers(q['answers']))


def post_request():
    post_data = {"id": "1", "correct": True, }
    return requests.post(QUIZ_URL, json=post_data).text


def get_correct_answer(questions):
    res = []
    for answer in questions.answers:
        if answer.correct:
            res.append(answer.answer)
    return res