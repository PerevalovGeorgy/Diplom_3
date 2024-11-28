from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import allure


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.timeout = 30

    def wait_element_and_find_element(self, locator):
        WebDriverWait(self.driver, self.timeout).until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    def wait_elements_and_find_elements(self, locator):
        WebDriverWait(self.driver, self.timeout).until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_elements(*locator)

    def wait_element_to_be_clickable_and_find_element(self, locator):
        WebDriverWait(self.driver, self.timeout).until(expected_conditions.element_to_be_clickable(locator))
        return self.driver.find_element(*locator)

    def base_click_element(self, locator):
        WebDriverWait(self.driver, self.timeout).until(expected_conditions.element_to_be_clickable(locator))
        self.wait_element_and_find_element(locator).click()

    def time_to_change_number(self,locator, dat):
        WebDriverWait(self.driver, self.timeout).until(expected_conditions.text_to_be_present_in_element(locator, dat))

    def add_text_in_element(self, locator, text):
        self.wait_element_and_find_element(locator).send_keys(text)

    def get_text_from_element(self, locator):
        return self.wait_element_and_find_element(locator).text

    def base_get_element_attribute(self, locator, atr):
        return self.wait_element_and_find_element(locator).get_attribute(atr)

    def get_url_page(self):
        return self.driver.current_url

    @allure.step('Клик по элементу в ФФ')
    def move_to_element_and_click(self, locator):
        WebDriverWait(self.driver, self.timeout).until(expected_conditions.element_to_be_clickable(locator))
        element = self.driver.find_element(*locator)
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click(element).perform()

    @allure.step('Drag an element and click on them  в ФАЕРФОКС ')
    def drag_and_drop_element(self, locator_from, locator_to):
        self.wait_element_and_find_element(locator_from)
        self.wait_element_and_find_element(locator_to)
        element_from = self.driver.find_element(*locator_from)
        element_to = self.driver.find_element(*locator_to)
        self.driver.execute_script('''
                       var source = arguments[0];
                       var target = arguments[1];
                       var evt = document.createEvent("DragEvent");
                       evt.initMouseEvent("dragstart", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
                       source.dispatchEvent(evt);
                       evt = document.createEvent("DragEvent");
                       evt.initMouseEvent("dragenter", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
                       target.dispatchEvent(evt);
                       evt = document.createEvent("DragEvent");
                       evt.initMouseEvent("dragover", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
                       target.dispatchEvent(evt);
                       evt = document.createEvent("DragEvent");
                       evt.initMouseEvent("drop", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
                       target.dispatchEvent(evt);
                       evt = document.createEvent("DragEvent");
                       evt.initMouseEvent("dragend", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
                       source.dispatchEvent(evt);
                       ''', element_from, element_to)

