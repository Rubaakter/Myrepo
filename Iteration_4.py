import requests
import json
QUESTIONS = "frågor.json"


URL = "https://bjornkjellgren.se/quiz/v1/questions"
QUESTION = requests.get(URL).json()


def load_question():
    try:
        with open(QUESTIONS, encoding='utf-8') as question:
            return json.load(question)
    except FileNotFoundError:
        with open(QUESTIONS, "w") as question:
                return


def my_questionnaire():
    print("EXEMPELKÖRNING:    \n'''''''\n")
    correct_answers = 0
    my_question = load_question()
    for i in my_question["questions"]:
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
    print(f"Du fick {str(correct_answers)} poäng av {str(len(my_question['questions']))}  möjliga.")


def main():
    print("EXEMPELKÖRNING:    \n'''''''\n")
    correct_answers = 0
    for i in QUESTION["questions"]:
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
    print(f"Du fick {str(correct_answers)} poäng av {str(len(QUESTION['questions']))}  möjliga.")


if __name__ == '__main__':
    my_questionnaire()
#        main()