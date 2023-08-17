import allure
from pages.base_page import BasePage
from locators import ScooterRentElements


class ScooterRentPage(BasePage):
    @allure.step("Click on delivery date placeholder")
    def click_on_delivery_date_placeholder(self):
        return self.find_element(ScooterRentElements.delivery_date_placeholder).click()

    @allure.step("Choose the final day of the final week")
    def choose_final_day_of_final_week_in_calendar(self):
        return self.find_element(ScooterRentElements.final_day_of_final_week_in_calendar).click()

    @allure.step("Click on rent duration placeholder")
    def click_on_rent_duration_placeholder(self):
        return self.find_element(ScooterRentElements.rent_duration_placeholder).click()

    @allure.step("Choose the first option for rent duration")
    def choose_first_duration_option(self):
        return self.find_element(ScooterRentElements.first_duration_option).click()

    @allure.step("Click on 'Order' button")
    def click_on_order_button_bottom(self):
        return self.find_element(ScooterRentElements.order_button_bottom).click()

    @allure.step("Click on 'Yes' button")
    def click_on_yes_button(self):
        return self.find_element(ScooterRentElements.yes_button).click()

    @allure.step("Click on 'Check status' button")
    def click_on_check_status_button(self):
        return self.find_element(ScooterRentElements.check_status_button).click()

    def fill_in_form_on_rent_page(self):
        self.click_on_delivery_date_placeholder()
        self.choose_final_day_of_final_week_in_calendar()
        self.click_on_rent_duration_placeholder()
        self.choose_first_duration_option()
