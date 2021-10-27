import random

from ITERATION_6_med_class.iteration_6_model import get_questions, post_request, get_correct_answer


def main():
    print(f"\n\nEXEMPELKÖRNING:    \nSlumpar fram 10 av  {str(len(get_questions()))} frågor. \n ")
    correct_answers = 0
    right_ans_of_user_mistakes = []
    random_questions = random.sample(get_questions(), 10)

    for qu_num, question in enumerate(random_questions,start=1):
        print(f"Fråga: {qu_num}. [{question.percent_correct()}] {question.prompt}")
        for i, answer in enumerate(question.answers, start=1):
            print(f"[{i}]] {answer}")

        try:
            user_answer = int(input("Ditt svar (1/2/3/4) : "))
            if question.answers[user_answer-1].correct:
                print("Rätt \n")
                correct_answers += 1
            else:
                print(f"fel svar. Rätt svar är : {' eller '.join(get_correct_answer(question))}  \n")
                right_ans_of_user_mistakes.append(f"- {question.prompt} ")
                right_ans_of_user_mistakes.append(f"Rätt svar är : {' eller '.join(get_correct_answer(question))}")

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
    main()
    post_request()
