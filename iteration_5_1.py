def print_answers(answers: list[dict]):
    for ans_num, answer in enumerate(answers, start=1):
        print(f"[{ans_num}] {answer['answer']}")


def get_correct_answers(answers: list[dict]) -> list[str]:
    res = []
    for answer in answers:
        if answer['correct']:
            res.append(answer['answer'])
    return res


def input_user_answer(answers, correct_answers, question, right_ans_of_user_mistakes):
    try:
        user_answer = int(input("Ditt svar (1/2/3/4) : "))
        if answers[user_answer - 1]['correct']:
            print("Rätt  \n")
            correct_answers += 1
        else:
            print(
                f"Fel svar, rätt svar är : {' eller '.join(get_correct_answers(answers))} \n")  # Användaren svarade fel
            right_ans_of_user_mistakes.append(f"- {question['prompt']} ")
            right_ans_of_user_mistakes.append(f"Rätt svar är : {' eller '.join(get_correct_answers(answers))}")
    except ValueError:
        print(f"Fel svar. Ange ett nummer istället.\n")
    except IndexError:
        print(f"Ange ett nummer inom 1-4.\n")
    return correct_answers