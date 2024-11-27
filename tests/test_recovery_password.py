import allure

from data import TestUrl
from pages.login_page import LoginPage
from pages.forgot_page import ForgotPage
from pages.reset_page import ResetPage


class TestRecoveryPassword:
    @allure.description("При прохождении теста выполняется проверка перехода на восстановление пароля")
    @allure.title("проверка перехода на восстановление пароля")
    def test_transition_to_recovery_password(self, driver):
        driver.get(TestUrl.url_login_page)
        login_page = LoginPage(driver)
        login_page.click_on_recovery_user_password()
        forgot_page = ForgotPage(driver)
        forgot_page.add_email_user()
        forgot_page.click_on_recovery_button()
        reset_page = ResetPage(driver)
        assert reset_page.get_text_from_recovery_title() == 'Введите код из письма', f"{reset_page.get_text_from_recovery_title()}"

    @allure.description("При прохождении теста выполняется проверка работы кнопки скрыть")
    @allure.title("проверка работы кнопки скрыть")
    def test_visible_button_make_password_visible(self, driver):
        driver.get(TestUrl.url_login_page)
        login_page = LoginPage(driver)
        login_page.add_password_user()
        login_page.click_on_visible_password_button()
        assert login_page.get_password_string_attribute() == 'text', f"{login_page.get_password_string_attribute()}"

