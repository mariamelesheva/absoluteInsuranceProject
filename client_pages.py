from helpers import BasePage, LocatorType


class City:
    krasnodar = 'г. Краснодар'


class TickBiteInsurancePolicyForm(BasePage):
    insured_persons_count = '.form-radio-list li'
    url = 'https://www.absolutins.ru/kupit-strahovoj-polis/strahovanie-zhizni-i-zdorovya/ukus-kleshcha/'
    header = '.calc-col-content__h1'
    region_select_btn = '[id="region-button"]'
    calculate_btn = '[data-caption="Рассчитать"]'
    tick = '//div[text()="Клещ"]'
    promocode_field = '[name="PROMOCODE"]'

    def open(self):
        self.browser.get(self.url)
        self.helper.wait_until_located(self.header, LocatorType.css)

    def choose_insure_persons_count(self, count: int):
        elem = self.helper.find_elements_by_locator(self.insured_persons_count)[count - 1]
        elem.click()

    def choose_region(self, city):
        self.helper.click_on_elem(self.region_select_btn)
        elem_locator = f"//div[text()='{city}']"
        self.helper.click_on_elem(elem_locator)

    def calculate(self):
        self.helper.click_on_elem(self.calculate_btn)
        calculate_form = CalculateForm(self.helper)
        return calculate_form

    def select_mite(self):
        self.helper.click_on_elem(self.tick)


class CalculateForm(BasePage):
    number = '#result-number'

    def check_sum(self, sum):
        locator_with_text = f'//span[contains(@id,"result-sum") and text()="{str(sum)} "]'
        self.helper.wait_until_located(locator_with_text, LocatorType.xpath)
        self.helper.find_element_by_locator(locator_with_text)

    def get_number_text(self):
        return self.helper.find_element_by_locator(self.number).text
