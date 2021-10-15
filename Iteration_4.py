import requests
import json
QUESTIONS = "frågor.json"

#For my questionnaire


def load_question():
    try:
        with open(QUESTIONS, encoding='utf-8') as question:
            return json.load(question)
    except FileNotFoundError:
        with open(QUESTIONS, "w") as question:
             return


def print_answers(answers: list[dict]):
    for ans_num, answer in enumerate(answers, start=1):
        print(f"[{ans_num}] {answer['answer']}")


def get_correct_answers(answers: list[dict]) -> list[str]:
    res = []
    for answer in answers:
        if answer['correct']:
            res.append(answer['answer'])
    return res


my_questions = load_question()
# for web questionnaire
URL = "https://bjornkjellgren.se/quiz/v1/questions"
question_web = requests.get(URL).json()


def main(questions=question_web):
    print("EXEMPELKÖRNING:    \n'''''''\n")
    correct_answers = 0
    for question in questions["questions"]:
        true_answer = ""
        print(question['id'], question['prompt'])
        answers = question['answers'] # Listan av svaren på den aktuella frågan
        print_answers(answers)
        try:
            user_answer = int(input("Ditt svar (1/2/3) : "))
            if answers[user_answer - 1]['correct']:
                print("Rätt")
                correct_answers += 1
            else:
                # Användaren svarade fel
                print(f"Fel svar, rätt svar är : {' eller '.join(get_correct_answers(answers))}")
        except ValueError:
           print(f"Fel svar. Ange ett nummer istället.")

    print(f"""**** RESULTAT ****""")
    print(f"Du fick {str(correct_answers)} poäng av {str(len(questions['questions']))}  möjliga.")


if __name__ == '__main__':
    main(questions=my_questions)

