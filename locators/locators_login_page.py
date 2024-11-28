from selenium.webdriver.common.by import By


class LocatorsLoginPage:
    TITLE_ENTER = By.XPATH, ".//h2[contains(text(),'Вход')]"
    INPUT_EMAIL_ENTER = By.XPATH, "//input[@name='name']"
    INPUT_PASSWORD_ENTER = By.XPATH, "//input[@name='Пароль']"
    ENTER_BUTTON = By.XPATH, "//button[contains(text(),'Войти')]"
    TITLE_RECOVERY_PASSWORD = By.XPATH, "//a[contains(@href,'/forgot-password')]"
    VISIBLE_BUTTON = By.XPATH, "//*[name()='path' and contains(@d,'M12 4C14.0')]"
    INPUT_PASSWORD_ENTER_VISIBLE = By.XPATH, "//input[@type='text' and @name='Пароль']"

