
import allure
from locators.locators_forgot_page import LocatorsForgotPage
from pages.base_page import BasePage
from data import UserData
from data import DRIVER_NAME


class ForgotPage(BasePage):
    @allure.step("вставить email")
    def add_email_user(self):
        self.add_text_in_element(LocatorsForgotPage.INPUT_EMAIL, UserData.email)

    @allure.step("нажать на кнопку восстановить")
    def click_on_recovery_button(self):
        if DRIVER_NAME == "chrome":
            self.base_click_element(LocatorsForgotPage.RECOVERY_BUTTON)
        else:
            self.move_to_element_and_click(LocatorsForgotPage.RECOVERY_BUTTON)

