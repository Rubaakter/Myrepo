import random
import requests
import json
from iteration_5_1 import print_answers, get_correct_answers

QUESTIONS = "frågor.json"


def load_question(): #For my questionnaire
    try:
        with open(QUESTIONS, encoding='utf-8') as question:
            return json.load(question)
    except FileNotFoundError:
        with open(QUESTIONS, "w") as question:
             return


my_questions = load_question()

URL = "https://bjornkjellgren.se/quiz/v2/questions" # for web questionnaire
question_web = requests.get(URL).json()


def post_request(questions=question_web):
    for question in questions['questions']:
        post_data = {"id": question['id'], "correct": question['answers']['correct']}
        print(requests.post(URL, json=post_data).text)


def percent_correct(questions=question_web):
    for question in questions['questions']:
        return f"{int(question['times_correct'])/int(question['times_asked']):.0%} har svarat rätt"


def main(questions=question_web):
    print(f"\n\nEXEMPELKÖRNING:    \nSlumpar fram 10 av {str(len(questions['questions']))} frågor. \n ")
    correct_answers = 0
    right_ans_of_user_mistakes = []
    random_questions = random.sample((questions["questions"]), 10)

    for qu_num, question in enumerate(random_questions, start=1):
        print(f"Fråga: {qu_num}. [{percent_correct()}] {question['prompt']}")
        answers = question['answers'] # Listan av svaren på den aktuella frågan
        print_answers(answers)
        try:
            user_answer = int(input("Ditt svar (1/2/3/4) : "))
            if answers[user_answer - 1]['correct']:
                print("Rätt  \n")
                correct_answers += 1
            else:
                print(f"Fel svar, rätt svar är : {' eller '.join(get_correct_answers(answers))} \n")  # Användaren svarade fel
                right_ans_of_user_mistakes.append(f"- {question['prompt']} ")
                right_ans_of_user_mistakes.append(f"Rätt svar är : {' eller '.join(get_correct_answers(answers))}")
        except ValueError:
            print(f"Fel svar. Ange ett nummer istället.\n")
        except IndexError:
            print(f"Ange ett nummer inom 1-4.\n")

    print(f"""\n**** RESULTAT ****""")
    print(f"Du fick {str(correct_answers)} poäng av 10  möjliga.\n\n")  # {str(len(questions['questions']))}

    print(f"Du svarade fel på dessa frågor: ")
    for ans in right_ans_of_user_mistakes:
        print(ans)


if __name__ == '__main__':
    main(questions=question_web)
    post_request()
#    main(questions=my_questions)

