from pages.feed_page import FeedPage
from pages.main_page import MainPage
from pages.general_metods import GeneralMetods
import time
import allure

class TestCountersOrders:

    @allure.description("При прохождении теста выполняется создание заказа с проверкой увеличения количества заказов за все время")
    @allure.title("проверка увеличеиня количества заказов за все время")
    def test_counter_orders_all_time_increase(self, driver_login):
        main_page = MainPage(driver_login)
        main_page.click_on_strip_order()
        feed_page = FeedPage(driver_login)
        q_all_time_before = int(feed_page.get_all_time_quantity())
        feed_page.click_on_constructor()
        main_page.add_loaf_in_order()
        main_page.click_on_place_on_order_button()
        main_page.click_close_button_on_order_place()
        main_page.click_on_strip_order()
        time.sleep(2)
        q_all_time_after = int(feed_page.get_all_time_quantity())
        assert q_all_time_after > q_all_time_before

    @allure.description("При прохождении теста выполняется создание заказа с проверкой увеличения количества заказов за все сегодня")
    @allure.title("проверка увеличеиня количества заказов за все сегодня")
    def test_counter_orders_to_day_increase(self, driver_login):
        main_page = MainPage(driver_login)
        main_page.click_on_strip_order()
        feed_page = FeedPage(driver_login)
        q_to_day_before = int(feed_page.get_to_day_quantity())
        feed_page.click_on_constructor()
        main_page.add_loaf_in_order()
        main_page.click_on_place_on_order_button()
        main_page.click_close_button_on_order_place()
        main_page.click_on_strip_order()
        time.sleep(2)
        q_to_day_after = int(feed_page.get_to_day_quantity())
        assert q_to_day_after > q_to_day_before


class TestOrdersInWork:

    @allure.description("При прохождении теста выполняется создание заказа с проверкой что заказ в работе")
    @allure.title("проверка наличия заказа в работе")
    def test_order_number_in_work_place(self, driver_login):
        main_page = MainPage(driver_login)
        main_page.add_loaf_in_order()
        main_page.click_on_place_on_order_button()
        number = int(main_page.get_number_of_order())
        main_page.click_close_button_on_order_place()
        main_page.click_on_strip_order()
        feed_page = FeedPage(driver_login)
        time.sleep(2)
        orders_in_work = feed_page.get_numbers_of_orders_in_work()
        assert number in orders_in_work


class TestOrdersDetail:
    @allure.description("При прохождении теста выполняется проверка детализации заказа")
    @allure.title("проверка детализации заказа")
    def test_open_order_detail(self, driver_login):
        main_page = MainPage(driver_login)
        main_page.click_on_strip_order()
        feed_page = FeedPage(driver_login)
        feed_page.click_on_last_order()
        assert feed_page.get_text_from_detail_order() == 'Cостав'


class TestOrderInOrdersFeed:
    @allure.description("При прохождении теста выполняется проверка появления заказа в общем количестве заказов")
    @allure.title("проверка наличпия заказа в ленте заказов")
    def test_new_order_in_orders_feed(self, driver_login):
        main_page = MainPage(driver_login)
        main_page.add_loaf_in_order()
        main_page.click_on_place_on_order_button()
        number = int(main_page.get_number_of_order())
        main_page.click_close_button_on_order_place()
        main_page.click_on_strip_order()
        feed_page = GeneralMetods(driver_login)
        time.sleep(2)
        orders_in_work = feed_page.get_number_orders_from_orders_feed()
        assert f'#0{number}' in orders_in_work

