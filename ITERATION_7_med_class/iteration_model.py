import requests
QUIZ_URL = "https://bjornkjellgren.se/quiz/v2/questions"


class Answer:
    """Return the class 'Answer' with related attributes answer and correct to keep them together."""
    answer: str
    correct: bool

    def __init__(self, answer, correct):
        """It is always executed when Answer is being initiated."""
        self.answer = answer
        self.correct = correct

    def __str__(self):
        """Implement the __str__ method to customize the string representation of answer"""
        return self.answer


class Question:
    """Return the class 'Question' with five related attributes to keep them together."""
    id: int
    prompt: str
    times_asked: int
    times_correct: int
    answers: list[Answer]

    def __init__(self, id_, prompt, times_asked, times_correct, answers: list[Answer]):
        """It will always be executed when Question is being initiated."""
        self.id = int(id_)
        self.prompt = prompt
        self.times_asked = int(times_asked)
        self.times_correct = int(times_correct)
        self.answers = answers

    def percent_correct(self) -> str:
        """Return percentage of times users give correct answer"""
        return f"{self.times_correct / self.times_asked:.0%} har svarat rätt"


def get_questions() -> list[Question]:
    """Get questions from 'web api' in the format of parse_question"""
    response = requests.get(QUIZ_URL).json()
    res = []
    for q in response['questions']:
        res.append(parse_question(q))
    return res


def parse_answers(answers) -> list[Answer]:
    """To convert data(Answer) in a certain format to increase usability."""
    res = []
    for a in answers:
        res.append(Answer(a['answer'], a['correct']))
    return res


def parse_question(q) -> Question:
    """To convert data(Question) in a certain format to increase usability."""
    return Question(q['id'], q['prompt'], q['times_asked'], q['times_correct'], parse_answers(q['answers']))


def post_request():
    """This function is used to send post request to 'web api' every time the code is run"""
    for question in get_questions():
        post_data = {"id": question.id, "correct": True, }
        post = requests.post(QUIZ_URL, json=post_data).text
    return post


def get_correct_answer(questions):
    """The function extract correct answer from web api data"""
    res = []
    for answer in questions.answers:
        if answer.correct:
            res.append(answer.answer)
    return res
