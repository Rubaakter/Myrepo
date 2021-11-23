import pytest
from iteration_model import Question, Answer, get_correct_answer


@pytest.fixture
def dummy_question():
    return Question(1, "Vilket år utvecklades Python", 50, 40,
                    [Answer("1991", True), Answer("1988", False), Answer("2000", False)])


@pytest.fixture
def dummy_question1():
    return Question(2, "Hur kan du kontrollera objektets typ?", 80, 55,
                    [Answer("type()", True), Answer("index()", False), Answer("typ()", False)])


def test_percent_correct(dummy_question):
    assert dummy_question.percent_correct() == "80% har svarat rätt"
    assert dummy_question.percent_correct() != 80


def test_percent_with_float_as_output(dummy_question1):
    assert dummy_question1.percent_correct() != "68.75% har svarat rätt"
    assert dummy_question1.percent_correct() == "69% har svarat rätt"


def test_get_correct_answer(dummy_question):
    assert get_correct_answer(dummy_question) == ['1991']
    assert get_correct_answer(dummy_question) != '2021'


def test_get_correct_answer2(dummy_question1):
    assert get_correct_answer(dummy_question1) == ['type()']
    assert get_correct_answer(dummy_question1) != 'type()'


def test_get_data(dummy_question):
    assert dummy_question.prompt == "Vilket år utvecklades Python"
    assert dummy_question.times_asked == 50
    assert dummy_question.times_correct == 40

