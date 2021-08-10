from selenium.common.exceptions import InvalidSelectorException
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LocatorType:
    css = 'css'
    xpath = 'xpath'


class Helper:
    def __init__(self):
        options = Options()
        options.add_argument('--start-maximized')
        self.browser = webdriver.Chrome(options=options)

    def click_on_elem(self, locator):
        elem = self.find_element_by_locator(locator)
        elem.click()

    def find_elements_by_locator(self, locator):
        try:
            return self.browser.find_elements_by_css_selector(locator)
        except InvalidSelectorException:
            return self.browser.find_elements_by_xpath(locator)

    def find_element_by_locator(self, locator):
        try:
            return self.browser.find_element_by_css_selector(locator)
        except InvalidSelectorException:
            return self.browser.find_element_by_xpath(locator)

    def wait_until_located(self, locator, locator_type, time=3):
        if locator_type == LocatorType.css:
            return WebDriverWait(self.browser, time).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, locator)),
                message=f'Элемент не найден по css локатору: {locator}')
        else:
            return WebDriverWait(self.browser, time).until(
                EC.presence_of_element_located((By.XPATH, locator)),
                message=f'Элемент не найден по xpath локатору: {locator}')


class BasePage:
    def __init__(self, helper: Helper):
        self.helper = helper
        self.browser = helper.browser
