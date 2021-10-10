import requests
#import json

URL = "https://bjornkjellgren.se/quiz/v1/questions"

questions = requests.get(URL).json()
#print(json.dumps(questions, indent=2))


def main():
    print("EXEMPELKÖRNING:    ")
    print("'''                      ")
    correct_answers = 0
    for i in questions["questions"]:
        true_answer = ""
        print(i['id'], i['prompt'])
        for j in i['answers']:
            print(j['answer'])
            if j['correct'] == True:
                true_answer = j['answer']
        answer = (input("Ditt svar : "))
        print(answer)
        if answer.lower() == true_answer:
            print("Rätt svar!")
            correct_answers += 1
        else:
            print("Fel svar")
            print(f"Rätt svar: {true_answer}")
        print(" "*80)
    print("                                      ")
    print(f"""**** RESULTAT ****""")
    print(f"Du fick {str(correct_answers)} poäng av {str(len(questions['questions']))}  möjliga.")


if __name__ == '__main__':
    main()