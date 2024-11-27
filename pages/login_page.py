
import allure
from locators.locators_login_page import LocatorsLoginPage
from pages.base_page import BasePage
from data import UserData, DRIVER_NAME


class LoginPage(BasePage):
    @allure.step("вставить email")
    def add_email_user(self):
        self.add_text_in_element(LocatorsLoginPage.INPUT_EMAIL_ENTER, UserData.email)

    @allure.step("вставить пароль")
    def add_password_user(self):
        self.add_text_in_element(LocatorsLoginPage.INPUT_PASSWORD_ENTER, UserData.password)

    @allure.step("клик на вход")
    def click_on_enter_button(self):
        if DRIVER_NAME == "chrome":
            self.base_click_element(LocatorsLoginPage.ENTER_BUTTON)
        else:
            self.move_to_element_and_click(LocatorsLoginPage.ENTER_BUTTON)

    @allure.step("клик на восстановить пароль")
    def click_on_recovery_user_password(self):
        if DRIVER_NAME == "chrome":
            self.base_click_element(LocatorsLoginPage.TITLE_RECOVERY_PASSWORD)
        else:
            self.move_to_element_and_click(LocatorsLoginPage.TITLE_RECOVERY_PASSWORD)

    @allure.step("клик на глазик")
    def click_on_visible_password_button(self):
        if DRIVER_NAME == "chrome":
            self.base_click_element(LocatorsLoginPage.VISIBLE_BUTTON)
        else:
            self.move_to_element_and_click(LocatorsLoginPage.VISIBLE_BUTTON)

    @allure.step("получить значение атрибута, для понимания что он перестал быть скрытым")
    def get_password_string_attribute(self):
        return self.base_get_element_attribute(LocatorsLoginPage.INPUT_PASSWORD_ENTER, 'type')

    @allure.step("получить текст со странице логина")
    def get_text_from_login_title(self):
        return self.get_text_from_element(LocatorsLoginPage.TITLE_ENTER)

