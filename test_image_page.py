from pages.main_page import MainPage
from pages.images_page import ImagePage



def test_pictures_on_yandex(browser):
    link = "https://yandex.ru/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_image_link()
    page.go_to_image_page()
    image_page = ImagePage(browser, browser.current_url)
    image_page.should_be_image_current_url()
    image_page.go_to_first_category()
    image_page.open_first_image()
    image_page.go_to_next_and_previous_image()
