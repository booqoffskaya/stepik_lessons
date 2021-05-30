from selenium import webdriver
from uuid import uuid4


def test_registration_and_login():
    url = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
    try:
        browser = webdriver.Chrome()
        browser.get(url)
        browser.implicitly_wait(5)

        # Генерируем данные для регистрации
        email = f'{uuid4()}@cats.ru'
        password = str(uuid4)

        # Шаг 1. Регистрирация пользователя
        registration_email = browser.find_element_by_name("registration-email")
        registration_email.send_keys(email)
        registration_password = browser.find_element_by_name("registration-password1")
        registration_password.send_keys(password)
        registration_password_2 = browser.find_element_by_name("registration-password2")
        registration_password_2.send_keys(password)

        button = browser.find_element_by_name("registration_submit")
        button.click()

        login_alert = browser.find_element_by_class_name("alertinner")
        message = login_alert.text

        successful_registration_msg = "Спасибо за регистрацию!"
        assert successful_registration_msg == message,\
            f'ОР: После успешной регистрации системой выводится сообщение "{successful_registration_msg}", ФР: {message}'

        # Шаг 2. Выход из системы
        logout_link = browser.find_element_by_id("logout_link")
        logout_link.click()

        exit_url = 'http://selenium1py.pythonanywhere.com/ru/'
        assert browser.current_url == exit_url,\
            f'ОР: После выхода из системы url = "{exit_url}", ФР: {browser.current_url}'

        # Шаг 3. Вход в систему под ранее зарегестрированным пользователем

        login_link = browser.find_element_by_id("login_link")
        login_link.click()

        login_email = browser.find_element_by_id("id_login-username")
        login_email.send_keys(email)

        login_password = browser.find_element_by_id("id_login-password")
        login_password.send_keys(password)

        button = browser.find_element_by_name('login_submit')
        button.click()

        login_alert = browser.find_element_by_class_name("alertinner")
        message = login_alert.text

        successful_login_msg = 'Рады видеть вас снова'
        assert successful_login_msg == message,\
            f'ОР: После успешного входа системой выводится сообщение "{successful_login_msg}", ФР: {message}'

    finally:
        browser.quit()


if __name__ == '__main__':
    test_registration_and_login()
