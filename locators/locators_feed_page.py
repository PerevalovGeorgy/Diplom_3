from selenium.webdriver.common.by import By


class LocatorsFeedPage:
    LAST_ORDER = By.XPATH, "(//li[@ class ='OrderHistory_listItem__2x95r mb-6'])[1]"
    TITLE_ORDERS_TO_DAY = By.XPATH, "//p[contains(text(),'Выполнено за сегодня:')]/parent::div/p[2]"
    TITLE_ORDERS_ALL_TIME = By.XPATH, "//p[contains(text(),'Выполнено за все')]/parent::div/p[2]"
    TITLE_ORDER_FEED = By.XPATH, "//h1[contains(text(),'Лента заказов')]"
    BUTTON_CONSTRUCTOR = By.XPATH, "//p[contains(text(),'Конструктор')]"
    LIST_ORDERS_IN_WORK = By.XPATH, "//ul[contains(@class, 'OrderFeed_orderListReady')]/li"
    TITLE_DETAIL_ORDER = By.CSS_SELECTOR, ".text.text_type_main-medium.mb-8"

