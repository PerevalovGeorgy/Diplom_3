
import allure
from locators.locators_reset_page import LocatorsResetPage
from pages.base_page import BasePage


class ResetPage(BasePage):
    @allure.step("текст с востановления")
    def get_text_from_recovery_title(self):
        return self.get_text_from_element(LocatorsResetPage.TITLE_INPUT_CODE)

