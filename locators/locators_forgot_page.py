from selenium.webdriver.common.by import By


class LocatorsForgotPage:
    RECOVERY_BUTTON = By.XPATH, "//button[contains(text(), 'Восстановить')]"
    INPUT_EMAIL = By.XPATH, "//input[@name='name']"

