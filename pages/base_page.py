import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Go to url')
    def go_to_site(self, base_url):
        return self.driver.get(base_url)

    def find_element(self, locator, time=5):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator), message=f'Not found {locator}')

    def scroll_to_element(self, locator):
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def wait_for_element(self, element):
        return WebDriverWait(self.driver, 3).until(EC.url_contains(element))