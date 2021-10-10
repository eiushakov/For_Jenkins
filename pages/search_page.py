from .base_page import BasePage
from .locators import SearchPageLocators


class SearchPage(BasePage):
    def should_be_table_of_search_result(self):
        assert self.is_element_present(*SearchPageLocators.SEARCH_TABLE, 4), "Table of search result is not presented"

    def should_be_link_in_search_result(self):
        search_link = "sovcombank.ru"
        search_elements = [el.text for el in self.browser.find_elements(*SearchPageLocators.LINK_LINES)]
        for i in range(5):
            assert search_elements[i].lower().find(search_link) != -1, f"{search_link} is not presented in {i + 1} search result"
