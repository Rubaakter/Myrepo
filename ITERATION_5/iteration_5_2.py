import json
import requests


def load_question(): #For my questionnaire
    QUESTIONS = "frågor.json"
    try:
        with open(QUESTIONS, encoding='utf-8') as question:
            return json.load(question)
    except FileNotFoundError:
        with open(QUESTIONS, "w") as question:
             return


URL = "https://bjornkjellgren.se/quiz/v2/questions" # for web questionnaire
question_web = requests.get(URL).json()


def post_request(questions=question_web):
    for question in questions['questions']:
        post_data = {"id": question['id'], "correct": True}
        return requests.post(URL, json=post_data).text


def print_answers(answers: list[dict]):
    for ans_num, answer in enumerate(answers, start=1):
        print(f"[{ans_num}] {answer['answer']}")


def get_correct_answers(answers: list[dict]) -> list[str]:
    res = []
    for answer in answers:
        if answer['correct']:
            res.append(answer['answer'])
    return res


def percent_correct(questions=question_web):
    for question in questions['questions']:
        return f"{int(question['times_correct'])/int(question['times_asked']):.0%} har svarat rätt"