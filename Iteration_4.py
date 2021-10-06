import json
QUESTIONS = "questions.json"


def load_question():
    try:
        with open(QUESTIONS) as question:
            return json.load(question)
    except FileNotFoundError:
        with open(QUESTIONS, "w") as question:
            return


def main():
    print("EXEMPELKÖRNING:    ")
    print("'''                      ")
    QUESTIONS = load_question()
    correct_answers = 0
    for i in QUESTIONS:
        print(i)
        answer = (input("Ditt svar (från 1/2/3): "))
        print(answer)
        if answer == QUESTIONS[i]:
            print("Rätt svar!")
            correct_answers += 1
        else:
            print("Fel svar")
            print(f"Rätt svar: {QUESTIONS[i]} ")

    print(f"""                                """)
    print(f"""**** RESULTAT ****""")
    print(f"Du fick {str(correct_answers)} poäng av {str(len(QUESTIONS))}  möjliga.")


if __name__ == '__main__':
    main()


# def load_questions():
#     try:
#         with open(QUESTIONS) as q:
#             return json.load(q)
#     except FileNotFoundError:
#         with open(QUESTIONS, "w") as q:
#             return
# def save_questions(questions):
#     with open(QUESTIONS, "r") as f:
#         json.dump(questions, f)
