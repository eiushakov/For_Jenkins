from .base_page import BasePage
from .locators import ImagesPageLocators


class ImagePage(BasePage):
    def should_be_image_current_url(self):
        images_url = "https://yandex.ru/images/?utm_source=main_stripe_big"
        self.browser.switch_to.window(self.browser.window_handles[1])
        assert self.browser.current_url == images_url, f"{images_url} is not current URL."

    def go_to_first_category(self):
        self.browser.find_element(*ImagesPageLocators.FIRST_CATEGORY).click()

    def open_first_image(self):
        self.browser.find_element(*ImagesPageLocators.FIRST_IMAGE).click()
        assert self.is_element_present(*ImagesPageLocators.OPEN_IMAGE, 4)

    def go_to_next_and_previous_image(self):
        first_image_url = self.browser.find_element(*ImagesPageLocators.CURRENT_IMAGE).get_attribute("src")
        self.browser.find_element(*ImagesPageLocators.NEXT_IMAGE_BUTTON).click()
        second_image_url = self.browser.find_element(*ImagesPageLocators.CURRENT_IMAGE).get_attribute("src")
        assert first_image_url != second_image_url, 'The second image is the same as the first'
        self.browser.find_element(*ImagesPageLocators.PREVIOUS_IMAGE_BUTTON).click()
        assert self.browser.find_element(*ImagesPageLocators.CURRENT_IMAGE).get_attribute("src") == first_image_url, 'The current picture is not the first'
