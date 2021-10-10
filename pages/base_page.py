from selenium.common.exceptions import NoSuchElementException, TimeoutException, NoAlertPresentException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from .locators import BasePageLocators


class BasePage:
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def should_be_search_line(self):
        assert self.is_element_present(*BasePageLocators.SEARCH_LINE), "Search line is not presented"

    def input_search_phrase(self):
        self.browser.find_element(*BasePageLocators.SEARCH_LINE).send_keys("Совкомбанк")

    def should_be_hint_table(self):
        assert self.is_element_present(*BasePageLocators.HINT_TABLE, 4), "Hint table is not presented"

    def should_be_phrase_in_hint_table(self):
        phrase = "Совкомбанк"
        text_content = self.browser.find_element(*BasePageLocators.HINT_TABLE)
        elements = [el.text for el in text_content.find_elements(*BasePageLocators.HINT_LINES)]
        for element in elements:
            assert element.lower().find(phrase.lower()) != -1, f"{phrase} is not presented in hint table."

    def go_to_search_result_page(self):
        self.browser.find_element(*BasePageLocators.SEARCH_LINE).send_keys(u'\ue007')

    def should_be_image_link(self):
        assert self.is_element_present(*BasePageLocators.PICTURES_LINK), "Pictures link is not presented"

    def go_to_image_page(self):
        link = self.browser.find_element(*BasePageLocators.PICTURES_LINK)
        link.click()

    def is_element_present(self, how, what, timeout=1):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        except NoSuchElementException:
            return False
        return True
