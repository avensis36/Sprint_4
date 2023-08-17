import allure
import pytest
from pages.scooter_main_page import ScooterMainPage
from pages.scooter_order_page import ScooterOrderPage
from pages.scooter_rent_page import ScooterRentPage
import locators


@allure.story('Test the positive scenario flow')
class TestPositiveFlowOrder:
    top_button = locators.ScooterButtons.order_button_top
    bottom_button = locators.ScooterButtons.order_button_bottom

    @allure.title('Test ordering the scooter of the positive scenario flow')
    @pytest.mark.parametrize('order_button', [bottom_button, top_button])
    def test_order_flow_leads_to_order_confirmed(self, driver, order_button):
        scooter_main_page = ScooterMainPage(driver)
        scooter_main_page.go_to_site(scooter_main_page.base_url)
        scooter_main_page.click_on_cookie_disappear_button()
        scooter_main_page.scroll_to_order_button(order_button)
        scooter_main_page.click_on_order_button(order_button)

        scooter_order_page = ScooterOrderPage(driver)
        scooter_order_page.fill_in_form_on_order_page('Тест', 'Тестов', 'Тестовый адрес', '11111111111')
        scooter_order_page.click_on_next_button()

        scooter_rent_page = ScooterRentPage(driver)
        scooter_rent_page.fill_in_form_on_rent_page()
        scooter_rent_page.click_on_order_button_bottom()
        scooter_rent_page.click_on_yes_button()

        actual_header = scooter_rent_page.find_element(locators.ScooterRentElements.order_is_confirmed_header).text
        assert "Заказ оформлен" in actual_header
