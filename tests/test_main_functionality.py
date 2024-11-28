import allure

from pages.feed_page import FeedPage
from pages.main_page import MainPage
from pages.profile_page import ProfilePage


class TestCrossoverPage:
    @allure.description("При прохождении теста выполняется проверка перехода на главную по контруктору")
    @allure.title("проверка перехода на главную по контруктору")
    def test_constructor_transition_to_main_page(self, driver_login):
        main_page = MainPage(driver_login)
        main_page.click_on_personal_account()
        profile_page = ProfilePage(driver_login)
        profile_page.click_on_constructor_transition()
        assert str(main_page.get_text_from_constructor()) == 'Соберите бургер'

    @allure.description("При прохождении теста выполняется проверка перехода на ленту заказов")
    @allure.title("проверка перехода на на ленту заказов")
    def test_transition_to_order_feed(self, driver_login):
        main_page = MainPage(driver_login)
        main_page.click_on_strip_order()
        feed_page = FeedPage(driver_login)
        assert str(feed_page.get_text_from_title_order_feed()) == 'Лента заказов'


class TestIngredientInfo:
    @allure.description("При прохождении теста выполняется проверка информации о ингредиенте")
    @allure.title("проверка информации о ингредиенте")
    def test_get_ingredient_info(self, driver_login):
        main_page = MainPage(driver_login)
        main_page.click_on_ingredient()
        assert main_page.get_text_from_ingredient_info() == 'Детали ингредиента'

    @allure.description("При прохождении теста выполняется проверка закрытия информации о ингредиенте")
    @allure.title("проверка закрытия информации о ингредиенте")
    def test_close_a_ingredient_info(self, driver_login):
        main_page = MainPage(driver_login)
        main_page.click_on_ingredient()
        main_page.click_on_close_ingredient_detail()
        assert main_page.order_button_on_main_page_a_clickable() is True


class TestIncreaseCounter:
    @allure.description("При прохождении теста выполняется проверка каунтера ингредиента")
    @allure.title("проверка каунтера ингредиента")
    def test_increase_counter(self,driver_login):
        main_page = MainPage(driver_login)
        main_page.add_loaf_in_order()
        assert main_page.get_counter_ingredient_loaf() == '2'


class TestLoginUserGetOrder:
    @allure.description("При прохождении теста выполняется проверка возможности создать заказ залогиненому пользователю")
    @allure.title("проверка возможности создать заказ залогиненому пользователю")
    def test_login_user_get_order(self,driver_login):
        main_page = MainPage(driver_login)
        main_page.add_loaf_in_order()
        main_page.add_sauce_in_order()
        main_page.click_on_place_on_order_button()
        assert main_page.get_identifier_order() == 'идентификатор заказа'

