from locators.locators_feed_page import LocatorsFeedPage
from pages.base_page import BasePage
from data import DRIVER_NAME
import allure


class FeedPage(BasePage):
    @allure.step("количество заказов за все время")
    def get_all_time_quantity(self):
        return self.get_text_from_element(LocatorsFeedPage.TITLE_ORDERS_ALL_TIME)

    @allure.step("количество заказов за все сегодня")
    def get_to_day_quantity(self):
        return self.get_text_from_element(LocatorsFeedPage.TITLE_ORDERS_TO_DAY)

    @allure.step("номер заказа в работе")
    def get_numbers_of_orders_in_work(self):
        self.wait_element_and_find_element(LocatorsFeedPage.TITLE_ORDER_FEED)
        numbers = self.wait_elements_and_find_elements(LocatorsFeedPage.LIST_ORDERS_IN_WORK)
        return [int(l.text) for l in numbers if l.text.isdigit()]

    @allure.step("текст на странице лента заказов")
    def get_text_from_title_order_feed(self):
        return self.get_text_from_element(LocatorsFeedPage.TITLE_ORDER_FEED)

    @allure.step("текст на деталях заказа")
    def get_text_from_detail_order(self):
        return self.get_text_from_element(LocatorsFeedPage.TITLE_DETAIL_ORDER)

    @allure.step("клик на конструктор")
    def click_on_constructor(self):
        if DRIVER_NAME == "chrome":
            self.base_click_element(LocatorsFeedPage.BUTTON_CONSTRUCTOR)
        else:
            self.move_to_element_and_click(LocatorsFeedPage.BUTTON_CONSTRUCTOR)

    @allure.step("клик на последний заказ")
    def click_on_last_order(self):
        if DRIVER_NAME == "chrome":
            self.base_click_element(LocatorsFeedPage.LAST_ORDER)
        else:
            self.move_to_element_and_click(LocatorsFeedPage.LAST_ORDER)

