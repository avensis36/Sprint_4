import allure
from locators import ScooterQuestions as q
from locators import ScooterAnswers as a
from pages.scooter_main_page import ScooterMainPage


@allure.story('Tests for correct answer appearances after click on each question')
class TestScooterQuestionBlock:

    @allure.feature('Check an appearance of the correct answer for question 1')
    def test_click_on_question_1_answer_1_appears(self, driver):
        scooter_main_page = ScooterMainPage(driver)
        scooter_main_page.go_to_site(scooter_main_page.base_url)
        scooter_main_page.scroll_to_question(q.question_1)
        scooter_main_page.click_on_question(q.question_1)
        actual_answer = scooter_main_page.find_answer(a.answer_1).text
        expected_answer = 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'
        assert actual_answer == expected_answer

    @allure.feature('Check an appearance of the correct answer for question 2')
    def test_click_on_question_2_answer_2_appears(self, driver):
        scooter_main_page = ScooterMainPage(driver)
        scooter_main_page.go_to_site(scooter_main_page.base_url)
        scooter_main_page.scroll_to_question(q.question_2)
        scooter_main_page.click_on_question(q.question_2)
        actual_answer = scooter_main_page.find_answer(a.answer_2).text
        expected_answer = 'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.'
        assert actual_answer == expected_answer

    @allure.feature('Check an appearance of the correct answer for question 3')
    def test_click_on_question_3_answer_3_appears(self, driver):
        scooter_main_page = ScooterMainPage(driver)
        scooter_main_page.go_to_site(scooter_main_page.base_url)
        scooter_main_page.scroll_to_question(q.question_3)
        scooter_main_page.click_on_question(q.question_3)
        actual_answer = scooter_main_page.find_answer(a.answer_3).text
        expected_answer = 'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.'
        assert actual_answer == expected_answer

    @allure.feature('Check an appearance of the correct answer for question 4')
    def test_click_on_question_4_answer_4_appears(self, driver):
        scooter_main_page = ScooterMainPage(driver)
        scooter_main_page.go_to_site(scooter_main_page.base_url)
        scooter_main_page.scroll_to_question(q.question_4)
        scooter_main_page.click_on_question(q.question_4)
        actual_answer = scooter_main_page.find_answer(a.answer_4).text
        expected_answer = 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'
        assert actual_answer == expected_answer

    @allure.feature('Check an appearance of the correct answer for question 5')
    def test_click_on_question_5_answer_5_appears(self, driver):
        scooter_main_page = ScooterMainPage(driver)
        scooter_main_page.go_to_site(scooter_main_page.base_url)
        scooter_main_page.scroll_to_question(q.question_5)
        scooter_main_page.click_on_question(q.question_5)
        actual_answer = scooter_main_page.find_answer(a.answer_5).text
        expected_answer = 'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.'
        assert actual_answer == expected_answer

    @allure.feature('Check an appearance of the correct answer for question 6')
    def test_click_on_question_6_answer_6_appears(self, driver):
        scooter_main_page = ScooterMainPage(driver)
        scooter_main_page.go_to_site(scooter_main_page.base_url)
        scooter_main_page.scroll_to_question(q.question_6)
        scooter_main_page.click_on_question(q.question_6)
        actual_answer = scooter_main_page.find_answer(a.answer_6).text
        expected_answer = 'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.'
        assert actual_answer == expected_answer

    @allure.feature('Check an appearance of the correct answer for question 7')
    def test_click_on_question_7_answer_7_appears(self, driver):
        scooter_main_page = ScooterMainPage(driver)
        scooter_main_page.go_to_site(scooter_main_page.base_url)
        scooter_main_page.scroll_to_question(q.question_7)
        scooter_main_page.click_on_question(q.question_7)
        actual_answer = scooter_main_page.find_answer(a.answer_7).text
        expected_answer = 'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.'
        assert actual_answer == expected_answer

    @allure.feature('Check an appearance of the correct answer for question 8')
    def test_click_on_question_8_answer_8_appears(self, driver):
        scooter_main_page = ScooterMainPage(driver)
        scooter_main_page.go_to_site(scooter_main_page.base_url)
        scooter_main_page.scroll_to_question(q.question_8)
        scooter_main_page.click_on_question(q.question_8)
        actual_answer = scooter_main_page.find_answer(a.answer_8).text
        expected_answer = 'Да, обязательно. Всем самокатов! И Москве, и Московской области.'
        assert actual_answer == expected_answer

