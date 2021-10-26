def print_answers(answers: list[dict]):
    for ans_num, answer in enumerate(answers, start=1):
        print(f"[{ans_num}] {answer['answer']}")


def get_correct_answers(answers: list[dict]) -> list[str]:
    res = []
    for answer in answers:
        if answer['correct']:
            res.append(answer['answer'])
    return res
