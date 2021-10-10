from pages.main_page import MainPage
from pages.search_page import SearchPage


def test_search_in_yandex(browser):
    link = "https://yandex.ru/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_search_line()
    page.input_search_phrase()
    page.should_be_hint_table()
    page.should_be_phrase_in_hint_table()
    page.go_to_search_result_page()
    search_page = SearchPage(browser, browser.current_url)
    search_page.should_be_table_of_search_result()
    search_page.should_be_link_in_search_result()
