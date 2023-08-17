import allure
import pytest
from locators import ScooterQuestions as q
from locators import ScooterAnswers as a
from pages.scooter_main_page import ScooterMainPage
from text_of_answers import ScooterAnswersText as answers_text


@allure.story('Tests for correct answer appearances after click on each question')
class TestScooterQuestionBlock:

    data = [[q.question_1, a.answer_1, answers_text.answer_1_text],
            [q.question_2, a.answer_2, answers_text.answer_2_text],
            [q.question_3, a.answer_3, answers_text.answer_3_text],
            [q.question_4, a.answer_4, answers_text.answer_4_text],
            [q.question_5, a.answer_5, answers_text.answer_5_text],
            [q.question_6, a.answer_6, answers_text.answer_6_text],
            [q.question_7, a.answer_7, answers_text.answer_7_text],
            [q.question_8, a.answer_8, answers_text.answer_8_text]]

    @pytest.mark.parametrize('question, answer, expected_answer', data)
    def test_click_on_questions_answers_appear(self, driver, question, answer, expected_answer):
        scooter_main_page = ScooterMainPage(driver)
        scooter_main_page.go_to_site(scooter_main_page.base_url)
        scooter_main_page.scroll_to_question(question)
        scooter_main_page.click_on_question(question)
        actual_answer = scooter_main_page.find_answer(answer).text
        assert actual_answer == expected_answer
