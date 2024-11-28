
import allure
from locators.locators_profile_page import LocatorsProfilePage
from pages.base_page import BasePage
from data import DRIVER_NAME


class ProfilePage(BasePage):
    @allure.step("клик на историю")
    def click_on_order_history(self):
        if DRIVER_NAME == "chrome":
            self.base_click_element(LocatorsProfilePage.TITLE_ORDER_HISTORY)
        else:
            self.move_to_element_and_click(LocatorsProfilePage.TITLE_ORDER_HISTORY)

    @allure.step("получить урл страницы")
    def get_url_list_of_orders(self):
        return self.get_url_page()

    @allure.step("выйти")
    def exit_from_profile(self):
        self.base_click_element(LocatorsProfilePage.LOGOUT_BUTTON)

    @allure.step("клик на контруктор")
    def click_on_constructor_transition(self):
        if DRIVER_NAME == "chrome":
            self.base_click_element(LocatorsProfilePage.DESIGNER_BUTTON)
        else:
            self.move_to_element_and_click(LocatorsProfilePage.DESIGNER_BUTTON)

