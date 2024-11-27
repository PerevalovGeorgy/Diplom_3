from selenium.webdriver.common.by import By


class LocatorsMainPage:
    PERSONAL_AC_BUTTON_CH = By.XPATH, ".//p[contains(text(),'Личный Кабинет')]"
    PERSONAL_AC_BUTTON_FF = By.XPATH, ".//p[contains(text(),'Личный Кабинет')]"
    SAUSE_SPACE = By.CSS_SELECTOR, "img[alt='Соус фирменный Space Sauce']"
    STRIP_BUTTON_FF = By.XPATH, "//p[contains(text(),'Лента Заказов')]"
    STRIP_BUTTON_CH = By.XPATH, "//p[contains(text(),'Лента Заказов')]"
    LOAF_CRATOR_BUTTON = By.XPATH, "//img[@src='https://code.s3.yandex.net/react/code/bun-02.png']"
    PLACE_ON_ORDER_BUTTON = By.XPATH, "//button[contains(text(),'Оформить заказ')]"
    TITLE_COLLECT_BURGER = By.CSS_SELECTOR, ".text.text_type_main-large.mt-10.mb-5"
    TITLE_INGREDIENT_DETAIL = By.XPATH, "//h2[contains(text(),'Детали ингредиента')]"
    CLOSE_BUTTON_INGREDIENT_DETAIL = By.CSS_SELECTOR, "section[class='Modal_modal_opened__3ISw4 Modal_modal__P3_V5'] button[type='button'] svg path"
    COUNTER_LOAF_CRATOR = By.XPATH, "//img[@alt='Краторная булка N-200i']/parent::a/div[@class='counter_counter__ZNLkj counter_default__28sqi']/p"
    TITLE_ORDER_INDIFICATION = By.CSS_SELECTOR, ".undefined.text.text_type_main-medium.mb-15"
    TITLE_ORDER_NUMBER = By.CSS_SELECTOR, ".Modal_modal__title_shadow__3ikwq.Modal_modal__title__2L34m.text.text_type_digits-large.mb-8"
    CLOSE_BUTTON_ORDER = By.XPATH, "//button[contains(@class, 'Modal_modal__close_modified__3V5XS')]"
    ORDER_PLACE = By.CSS_SELECTOR, ".BurgerConstructor_basket__list__l9dp_"

