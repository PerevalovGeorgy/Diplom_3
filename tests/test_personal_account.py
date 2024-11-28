import allure
from data import TestUrl
from pages.profile_page import ProfilePage
from pages.main_page import MainPage
from pages.login_page import LoginPage


class TestPersonalAccount:
    @allure.description("При прохождении теста выполняется проверка перехода на страницу истории")
    @allure.title("проверка перехода на страницу истории")
    def test_go_to_order_list(self, driver_login):
        main_page = MainPage(driver_login)
        main_page.click_on_personal_account()
        profile_page = ProfilePage(driver_login)
        profile_page.click_on_order_history()
        assert str(profile_page.get_url_list_of_orders()) == TestUrl.URL_HISTORY_PAGE

    @allure.description("При прохождении теста выполняется проверка выхода")
    @allure.title("проверка выхода")
    def test_logout(self, driver_login):
        main_page = MainPage(driver_login)
        main_page.click_on_personal_account()
        profile_page = ProfilePage(driver_login)
        profile_page.exit_from_profile()
        login_page = LoginPage(driver_login)
        assert str(login_page.get_text_from_login_title()) == "Вход"

