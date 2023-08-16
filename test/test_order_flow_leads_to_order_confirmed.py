import allure
import pytest
from pages.scooter_main_page import ScooterMainPage
from pages.scooter_order_page import ScooterOrderPage
from pages.scooter_rent_page import ScooterRentPage
from pages.base_page import BasePage
import locators


@allure.story('Test the positive scenario flow')
class TestPositiveFlow:
    top_button = locators.ScooterButtons.order_button_top
    bottom_button = locators.ScooterButtons.order_button_bottom

    @allure.feature('Test ordering the scooter of the positive scenario flow')
    @pytest.mark.parametrize('order_button, name, surname, address, phone',
                             [[bottom_button, 'Тест', 'Тестов', 'Тестовый адрес', '11111111111'],
                              [top_button, 'Иван', 'Иванов', 'Ул. Иванова 1', '89991112233']])
    def test_order_flow_leads_to_order_confirmed(self, driver, order_button, name, surname, address, phone):
        scooter_main_page = ScooterMainPage(driver)
        scooter_main_page.go_to_site(scooter_main_page.base_url)
        scooter_main_page.click_on_cookie_disappear_button()
        scooter_main_page.scroll_to_order_button(order_button)
        scooter_main_page.click_on_order_button(order_button)

        scooter_order_page = ScooterOrderPage(driver)
        scooter_order_page.fill_in_form_on_order_page(name, surname, address, phone)
        scooter_order_page.click_on_next_button()

        scooter_rent_page = ScooterRentPage(driver)
        scooter_rent_page.fill_in_form_on_rent_page()
        scooter_rent_page.click_on_order_button_bottom()
        scooter_rent_page.click_on_yes_button()

        actual_header = scooter_rent_page.find_element(locators.ScooterRentElements.order_is_confirmed_header).text
        assert "Заказ оформлен" in actual_header

    @allure.feature("Test clicking on 'Scooter' of the positive scenario flow")
    @pytest.mark.parametrize('order_button, name, surname, address, phone',
                             [[bottom_button, 'Тест', 'Тестов', 'Тестовый адрес', '11111111111'],
                              [top_button, 'Иван', 'Иванов', 'Ул. Иванова 1', '89991112233']])
    def test_order_flow_click_on_scooter_logo_after_order_is_confirmed(self, driver, order_button, name, surname, address, phone):
        self.test_order_flow_leads_to_order_confirmed(driver, order_button, name, surname, address, phone)

        scooter_rent_page = ScooterRentPage(driver)
        scooter_rent_page.click_on_check_status_button()

        scooter_main_page = ScooterMainPage(driver)
        scooter_main_page.click_on_scooter_logo()

        main_page_url = 'https://qa-scooter.praktikum-services.ru/'
        assert main_page_url == driver.current_url

    @allure.feature("Test clicking on 'Yandex' logo of the positive scenario flow")
    @pytest.mark.parametrize('order_button, name, surname, address, phone',
                             [[bottom_button, 'Тест', 'Тестов', 'Тестовый адрес', '11111111111'],
                              [top_button, 'Иван', 'Иванов', 'Ул. Иванова 1', '89991112233']])
    def test_order_flow_click_on_yandex_logo_leads_to_yandex_main_page(self, driver, order_button, name, surname, address, phone):
        self.test_order_flow_click_on_scooter_logo_after_order_is_confirmed(driver, order_button, name, surname, address, phone)

        scooter_main_page = ScooterMainPage(driver)
        scooter_main_page.click_on_yandex_logo()

        yandex_main_page_url = 'https://dzen.ru/?yredirect=true'
        driver.switch_to.window(driver.window_handles[1])
        base_page = BasePage(driver)
        base_page.wait_for_element(yandex_main_page_url)
        assert yandex_main_page_url == driver.current_url, f"Current url doesn't lead to {yandex_main_page_url}"

    @allure.feature('The whole flow')
    @pytest.mark.parametrize('order_button, name, surname, address, phone',
                             [[bottom_button, 'Тест', 'Тестов', 'Тестовый адрес', '11111111111'],
                              [top_button, 'Иван', 'Иванов', 'Ул. Иванова 1', '89991112233']])
    def test_the_whole_order_flow(self, driver, order_button, name, surname, address, phone):
        self.test_order_flow_click_on_yandex_logo_leads_to_yandex_main_page(driver, order_button, name, surname, address, phone)


