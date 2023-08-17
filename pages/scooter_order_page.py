import allure
from pages.base_page import BasePage
from locators import ScooterOrderElements


class ScooterOrderPage(BasePage):
    @allure.step('Fill in name')
    def fill_in_name(self, name):
        name_field = self.find_element(ScooterOrderElements.name_placeholder)
        name_field.click()
        name_field.send_keys(name)
        return name_field

    @allure.step('Fill in surname')
    def fill_in_surname(self, surname):
        surname_field = self.find_element(ScooterOrderElements.surname_placeholder)
        surname_field.click()
        surname_field.send_keys(surname)
        return surname_field

    def fill_in_address(self, address):
        address_filed = self.find_element(ScooterOrderElements.address_placeholder)
        address_filed.click()
        address_filed.send_keys(address)
        return address_filed

    @allure.step('Click on metro station')
    def click_on_metro_station(self):
        return self.find_element(ScooterOrderElements.metro_station_placeholder).click()

    @allure.step('Choose first metro station')
    def choose_first_metro_station(self):
        return self.find_element(ScooterOrderElements.first_metro_station).click()

    @allure.step('Fill in phone number')
    def fill_in_phone_number(self, phone):
        phone_field = self.find_element(ScooterOrderElements.phone_placeholder)
        phone_field.click()
        phone_field.send_keys(phone)
        return phone_field

    @allure.step('Click on Next button')
    def click_on_next_button(self):
        return self.find_element(ScooterOrderElements.next_button).click()

    @allure.step('Fill in form on order page')
    def fill_in_form_on_order_page(self, name, surname, address, phone):
        self.fill_in_name(name)
        self.fill_in_surname(surname)
        self.fill_in_address(address)
        self.click_on_metro_station()
        self.choose_first_metro_station()
        self.fill_in_phone_number(phone)