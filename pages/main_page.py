
import allure
from locators.locators_main_page import LocatorsMainPage
from pages.base_page import BasePage
from data import DRIVER_NAME


class MainPage(BasePage):
    @allure.step("клик на личный кабинет")
    def click_on_personal_account(self):
        if DRIVER_NAME == "chrome":
            self.base_click_element(LocatorsMainPage.PERSONAL_AC_BUTTON_CH)
        else:
            self.move_to_element_and_click(LocatorsMainPage.PERSONAL_AC_BUTTON_FF)

    @allure.step("клик на ингредиент")
    def click_on_ingredient(self):
        if DRIVER_NAME == "chrome":
            self.base_click_element(LocatorsMainPage.LOAF_CRATOR_BUTTON)
        else:
            self.move_to_element_and_click(LocatorsMainPage.LOAF_CRATOR_BUTTON)

    @allure.step("клик на кнопку закрыть")
    def click_on_close_ingredient_detail(self):
        if DRIVER_NAME == "chrome":
            self.base_click_element(LocatorsMainPage.CLOSE_BUTTON_INGREDIENT_DETAIL)
        else:
            self.move_to_element_and_click(LocatorsMainPage.CLOSE_BUTTON_INGREDIENT_DETAIL)

    @allure.step("клик на сделать заказ")
    def click_on_place_on_order_button(self):
        if DRIVER_NAME == "chrome":
            self.base_click_element(LocatorsMainPage.PLACE_ON_ORDER_BUTTON)
        else:
            self.move_to_element_and_click(LocatorsMainPage.PLACE_ON_ORDER_BUTTON)

    @allure.step("клик на ленту заказов")
    def click_on_strip_order(self):
        if DRIVER_NAME == "chrome":

            self.base_click_element(LocatorsMainPage.STRIP_BUTTON_CH)
        else:

            self.move_to_element_and_click(LocatorsMainPage.STRIP_BUTTON_FF)

    @allure.step("получить количество")
    def get_counter_ingredient_loaf(self):
        return self.get_text_from_element(LocatorsMainPage.COUNTER_LOAF_CRATOR)

    @allure.step("получить номер")
    def get_identifier_order(self):
        self.wait_element_to_be_clickable_and_find_element(LocatorsMainPage.CLOSE_BUTTON_ORDER)
        return self.get_text_from_element(LocatorsMainPage.TITLE_ORDER_INDIFICATION)

    @allure.step("получить текс из конструктора")
    def get_text_from_constructor(self):
        return self.get_text_from_element(LocatorsMainPage.TITLE_COLLECT_BURGER)

    @allure.step("получить текст с ингредиента")
    def get_text_from_ingredient_info(self):
        return self.get_text_from_element(LocatorsMainPage.TITLE_INGREDIENT_DETAIL)

    @allure.step("проверитьчто кнопка кликабельна")
    def order_button_on_main_page_a_clickable(self):
        self.wait_element_to_be_clickable_and_find_element(LocatorsMainPage.PLACE_ON_ORDER_BUTTON)
        return True

    @allure.step("номер заказа")
    def get_number_of_order(self):
        self.time_to_change_number(LocatorsMainPage.TITLE_ORDER_NUMBER, '15')
        return self.get_text_from_element(LocatorsMainPage.TITLE_ORDER_NUMBER)

    @allure.step("закрыть заказ")
    def click_close_button_on_order_place(self):
        self.time_to_change_number(LocatorsMainPage.TITLE_ORDER_NUMBER, '15')
        if DRIVER_NAME == "chrome":
            self.base_click_element(LocatorsMainPage.CLOSE_BUTTON_ORDER)
        else:
            self.move_to_element_and_click(LocatorsMainPage.CLOSE_BUTTON_ORDER)

    @allure.step("добавить булку")
    def add_loaf_in_order(self):
        self.drag_and_drop_element(LocatorsMainPage.LOAF_CRATOR_BUTTON, LocatorsMainPage.ORDER_PLACE)

    @allure.step("добавить соус")
    def add_sauce_in_order(self):
        self.drag_and_drop_element(LocatorsMainPage.SAUSE_SPACE, LocatorsMainPage.ORDER_PLACE)

