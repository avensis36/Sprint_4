from selenium.webdriver.common.by import By


class ScooterQuestions:
    question_1 = (By.ID, "accordion__heading-0")
    question_2 = (By.ID, "accordion__heading-1")
    question_3 = (By.ID, "accordion__heading-2")
    question_4 = (By.ID, "accordion__heading-3")
    question_5 = (By.ID, "accordion__heading-4")
    question_6 = (By.ID, "accordion__heading-5")
    question_7 = (By.ID, "accordion__heading-6")
    question_8 = (By.ID, "accordion__heading-7")


class ScooterAnswers:
    answer_1 = (By.ID, "accordion__panel-0")
    answer_2 = (By.ID, "accordion__panel-1")
    answer_3 = (By.ID, "accordion__panel-2")
    answer_4 = (By.ID, "accordion__panel-3")
    answer_5 = (By.ID, "accordion__panel-4")
    answer_6 = (By.ID, "accordion__panel-5")
    answer_7 = (By.ID, "accordion__panel-6")
    answer_8 = (By.ID, "accordion__panel-7")

class ScooterButtons:
    cookie_disappear_button = (By.CLASS_NAME, "App_CookieButton__3cvqF")  # Кнопка "да все привыкли"
    scooter_logo = (By.XPATH, ".//img[@alt='Scooter']")  # Логотип "Самокат"
    yandex_logo = (By.XPATH, ".//img[@alt='Yandex']")  # Логотип "Яндекс"
    order_button_top = (By.CLASS_NAME, "Button_Button__ra12g")  # Кнопка "Заказать вверху страницы"
    order_button_bottom = (By.XPATH,
                           ".//button[contains(@class, 'Button_Middle__1CSJM')]")  # Кнопка "Заказать вверху страницы"

class ScooterOrderElements:
    name_placeholder = (By.XPATH, ".//input[@placeholder='* Имя']")  # Плейсхолдер имени
    surname_placeholder = (By.XPATH, ".//input[@placeholder='* Фамилия']")  # Плейсхолдер фамилии
    address_placeholder = (By.XPATH, ".//input[@placeholder='* Адрес: куда привезти заказ']")  # Плейсхолдер адреса
    metro_station_placeholder = (By.CLASS_NAME, "select-search__input")  # Плейсхолдер станции метро
    first_metro_station = (By.XPATH, ".//li[@data-index='0']")  # Первая станция в списке метро
    phone_placeholder = (By.XPATH, ".//input[@placeholder='* Телефон: на него позвонит курьер']")  # Плейсхолдер номера телефона
    next_button = (By.XPATH, ".//button[text()='Далее']")  # Кнопка "Далее"

class ScooterRentElements:
    delivery_date_placeholder = (By.XPATH, ".//input[@placeholder='* Когда привезти самокат']")  # Плейсхолдер даты доставки самоката
    final_day_of_final_week_in_calendar = (By.XPATH,
                                           ".//div[@class='react-datepicker__week'][last()]/div[last()]")  # Последний день последней недели, который виден в календаре
    rent_duration_placeholder = (By.CLASS_NAME, "Dropdown-placeholder")  # Плейсхолдер продолжительности аренды
    first_duration_option = (By.XPATH, ".//div[@class='Dropdown-option'][1]")  # Первый вариант срока аренды
    order_button_bottom = (By.XPATH,
                           ".//button[@class='Button_Button__ra12g Button_Middle__1CSJM']")  # Кнопка "Заказать" внизу страницы
    yes_button = (By.XPATH, ".//button[text()='Да']")  # Кнопеп "Да" в окне "Хотите оформить заказ?"
    order_is_confirmed_header = (By.CLASS_NAME, "Order_ModalHeader__3FDaJ")  # Заголовок окна "Заказ оформлен"
    check_status_button = (By.XPATH, ".//button[text()='Посмотреть статус']")  # Кнопка "Посмотреть статус"



