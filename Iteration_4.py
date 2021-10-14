import requests
import json
QUESTIONS = "frågor.json"


def load_question():
    try:
        with open(QUESTIONS, encoding='utf-8') as question:
            return json.load(question)
    except FileNotFoundError:
        with open(QUESTIONS, "w") as question:
                return


my_questions = load_question()

URL = "https://bjornkjellgren.se/quiz/v1/questions"
question_web = requests.get(URL).json()


def main(query=question_web):
    print("EXEMPELKÖRNING:    \n'''''''\n")
    correct_answers = 0
    for i in query["questions"]:
        true_answer = ""
        print(i['id'], i['prompt'])
        for j in i['answers']:
            print(j['answer'])
            if j['correct'] == True:
                true_answer = j['answer']
        answer = (input("Ditt svar : "))
        print(answer)
        if answer.lower().strip() == true_answer:
            print("Rätt svar!   \n")
            correct_answers += 1
        else:
            print("Fel svar")
            print(f"Rätt svar: {true_answer}  \n")
    print(f"""**** RESULTAT ****""")
    print(f"Du fick {str(correct_answers)} poäng av {str(len(query['questions']))}  möjliga.")


if __name__ == '__main__':
    main(query=my_questions)

