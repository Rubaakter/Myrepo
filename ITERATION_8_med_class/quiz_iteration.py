import random
from ITERATION_8_med_class.iteration_model import get_questions, post_request, get_correct_answer
questions = get_questions()


def main():
    """Print all decorations to give the output a certain format.
    Call functions to implement them (post_request, printing_question_answer).
    Gather and print all correct answers where users give wrong answer"""

    print(f"\n\n\033[97mEXEMPELKÖRNING:    \n\033[92mSlumpar fram 10 av  {str(len(questions))} frågor. \n ")

    correct_answers = 0
    right_ans_of_user_mistakes = []
    random_questions = random.sample(questions, 10)
    correct_answers = printing_question_answer(correct_answers, random_questions, right_ans_of_user_mistakes)

    print(f"""\n**** RESULTAT ****""")
    print(f"\033[97mDu fick {str(correct_answers)} poäng av 10  möjliga.\n\n")  # {str(len(questions['questions']))}

    print(f"\033[94mDu svarade fel på dessa frågor: ")
    for ans in right_ans_of_user_mistakes:
        print(f"\033[97m{ans}")


def printing_question_answer(correct_answers, random_questions, right_ans_of_user_mistakes):
    """This function print questions and answers from 'web api data' and take users answer as input.
    Identify whether answer is correct or wrong and and handle any incorrect input of users"""

    for qu_num, question in enumerate(random_questions, start=1):
        print(f"\033[97mFråga: {qu_num}. \033[96m[{question.percent_correct()}] \033[97m{question.prompt}")
        for i, answer in enumerate(question.answers, start=1):
            print(f"\033[97m[{i}] {answer}")
        try:
            user_answer = int(input("\033[94mDitt svar : "))
            if question.answers[user_answer - 1].correct:
                print("\033[94mRätt \n")
                post_request(question.id, True)
                correct_answers += 1
            else:
                post_request(question.id, False)
                print(f"\033[96mFel svar. Rätt svar är : {' eller '.join(get_correct_answer(question))}  \n")
                right_ans_of_user_mistakes.append(f"- {question.prompt} ")
                right_ans_of_user_mistakes.append(f"Rätt svar är : {' eller '.join(get_correct_answer(question))}")
        except ValueError:
            print(f"\033[94mFel svar. Ange ett nummer istället.\n")
        except IndexError:
            print(f"\033[94mAnge ett nummer inom 1-4.\n")
    return correct_answers


if __name__ == '__main__':
    main()
