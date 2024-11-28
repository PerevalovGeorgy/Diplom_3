from selenium.webdriver.common.by import By


class LocatorsProfilePage:
    TITLE_ORDER_HISTORY = By.XPATH, "//a[contains(text(),'История заказов')]"
    LOGOUT_BUTTON = By.XPATH, "// button[contains(text(), 'Выход')]"
    DESIGNER_BUTTON = By.XPATH, ".//p[text()='Конструктор']"

