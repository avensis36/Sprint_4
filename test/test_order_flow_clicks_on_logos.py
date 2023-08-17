import locators
from pages.base_page import BasePage
from pages.scooter_main_page import ScooterMainPage
from pages.scooter_rent_page import ScooterRentPage


class TestPositiveFlowLogos:

    top_button = locators.ScooterButtons.order_button_top
    bottom_button = locators.ScooterButtons.order_button_bottom

    @allure.feature("Test clicking on 'Scooter' of the positive scenario flow")
    def test_order_flow_click_on_scooter_logo_after_order_is_confirmed(self, driver):
        self.test_order_flow_leads_to_order_confirmed(driver, TestPositiveFlowLogos.top_button)

        scooter_rent_page = ScooterRentPage(driver)
        scooter_rent_page.click_on_check_status_button()

        scooter_main_page = ScooterMainPage(driver)
        scooter_main_page.click_on_scooter_logo()

        main_page_url = 'https://qa-scooter.praktikum-services.ru/'
        assert main_page_url == driver.current_url

    @allure.feature("Test clicking on 'Yandex' logo of the positive scenario flow")
    def test_order_flow_click_on_yandex_logo_leads_to_yandex_main_page(self, driver):
        self.test_order_flow_click_on_scooter_logo_after_order_is_confirmed(driver)

        scooter_main_page = ScooterMainPage(driver)
        scooter_main_page.click_on_yandex_logo()

        yandex_main_page_url = 'https://dzen.ru/?yredirect=true'
        driver.switch_to.window(driver.window_handles[1])
        base_page = BasePage(driver)
        base_page.wait_for_element(yandex_main_page_url)
        assert yandex_main_page_url == driver.current_url, f"Current url doesn't lead to {yandex_main_page_url}"