import requests
import random

from ITERATION_6.iteration_6_1 import Answer, Question

QUIZ_URL = "https://bjornkjellgren.se/quiz/v2/questions"


def get_questions() -> list[Question]:
    response = requests.get(QUIZ_URL).json()
    res = []
    for q in response['questions']:
        # Här skall vi "parsa" en fråga och lägga till i listan res
        res.append(parse_question(q))
    return res


def parse_answers(answers) -> list[Answer]:
    res = []
    for a in answers:
        res.append(Answer(a['answer'], a['correct']))
    return res


def parse_question(q) -> Question:
    return Question(q['id'], q['prompt'], q['times_asked'], q['times_correct'], parse_answers(q['answers']))


def get_correct_answers(parse_answers):
    res = []
    for answer in parse_answers():
        if answer.correct:
            res.append(answer.correct)
    return res


def input_user_answer(answers, correct_answers, question, right_ans_of_user_mistakes):
    try:
        user_answer = int(input("Ditt svar (1/2/3/4) : "))
        if answer.correct == [user_answer - 1]:
            print("Rätt  \n")
            correct_answers += 1
        else:
            print(
                f"Fel svar, rätt svar är : {' eller '.join(get_correct_answers(answers))} \n")  # Användaren svarade fel
            right_ans_of_user_mistakes.append(f"- {question.prompt} ")
            right_ans_of_user_mistakes.append(f"Rätt svar är : {' eller '.join(get_correct_answers(answers))}")
    except ValueError:
        print(f"Fel svar. Ange ett nummer istället.\n")
    except IndexError:
        print(f"Ange ett nummer inom 1-4.\n")
    return correct_answers


if __name__ == '__main__':
    correct_answers = 0
    right_ans_of_user_mistakes = []
    random_questions = random.sample(get_questions(), 10)

    for qu_num, question in enumerate(random_questions, start=1):
        print(f"Fråga:{qu_num}. [{question.percent_correct()} har svarat rätt]  {question.prompt}")
        answers = question.answers
        for i, answer in enumerate(question.answers, start=1):
            print(f"[{i}]] {answer}")
        correct_answers = input_user_answer(answers, correct_answers, question, right_ans_of_user_mistakes)
        print("-" * 80)



#q = Question(2, "Vad är klasser bra till?", 5, 2, [Answer("Det är en smidig abstraktion", True), Answer("foo", False)])

# print(q.prompt)
# for i, a in enumerate(q.answers, start=1):
#     print(f"[{i}] {a}")