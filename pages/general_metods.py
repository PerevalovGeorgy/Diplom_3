from pages.base_page import BasePage
from selenium.webdriver.common.by import By
import allure


class GeneralMetods(BasePage):
    @allure.step("вспомгательный шаг для получения списка заказов из ленты заказов")
    def get_number_orders_from_orders_feed(self):
        numb_ord = []
        for i in range(1, 50):
            locator = f"(//div[@class='OrderHistory_textBox__3lgbs mb-6']/p[1])[{i}]"
            num = self.get_text_from_element([By.XPATH, locator])
            numb_ord.append(num)
        return numb_ord

