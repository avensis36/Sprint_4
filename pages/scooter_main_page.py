import allure
from pages.base_page import BasePage
from locators import ScooterButtons


class ScooterMainPage(BasePage):

    @property
    def base_url(self):
        base_url = 'https://qa-scooter.praktikum-services.ru/'
        return base_url

    @allure.step('Make cookie pop-up disappear')
    def click_on_cookie_disappear_button(self):
        return self.find_element(ScooterButtons.cookie_disappear_button).click()

    @allure.step('Click on a question')
    def click_on_question(self, question):
        return self.find_element(question).click()

    @allure.step('Scroll to a question')
    def scroll_to_question(self, question):
        return self.scroll_to_element(question)

    @allure.step('Find answer')
    def find_answer(self, answer):
        return self.find_element(answer)

    @allure.step("Scroll to necessary 'Order' button")
    def scroll_to_order_button(self, order_button):
        return self.scroll_to_element(order_button)

    @allure.step("Click on necessary 'Order' button")
    def click_on_order_button(self, order_button):
        necessary_order_button = self.find_element(order_button)
        necessary_order_button.click()
        return necessary_order_button

    @allure.step("Click on 'Scooter' logo")
    def click_on_scooter_logo(self):
        return self.find_element(ScooterButtons.scooter_logo).click()

    @allure.step("Click on 'Yandex' logo")
    def click_on_yandex_logo(self):
        return self.find_element(ScooterButtons.yandex_logo).click()
