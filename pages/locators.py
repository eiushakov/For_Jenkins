from selenium.webdriver.common.by import By


class BasePageLocators:
    SEARCH_LINE = (By.ID, "text")
    HINT_TABLE = (By.CSS_SELECTOR, '.mini-suggest__popup.mini-suggest__popup_theme_flat.mini-suggest__popup_visible')
    HINT_LINES = (By.CSS_SELECTOR, 'ul li')
    PICTURES_LINK = (By.CSS_SELECTOR, 'a[data-id="images"]')


class SearchPageLocators:
    SEARCH_TABLE = (By.ID, "search-result")
    LINK_LINES = (By.CSS_SELECTOR, '#search-result > li a > b')


class ImagesPageLocators:
    FIRST_CATEGORY = (By.CSS_SELECTOR, '.PopularRequestList-Item.PopularRequestList-Item_pos_0')
    FIRST_IMAGE = (By.CSS_SELECTOR, '.serp-item.serp-item_type_search.serp-item_group_search.serp-item_pos_0')
    OPEN_IMAGE = (By.CSS_SELECTOR, '.MMImage-Origin')
    NEXT_IMAGE_BUTTON = (By.CSS_SELECTOR, '.CircleButton.CircleButton_type_next')
    PREVIOUS_IMAGE_BUTTON = (By.CSS_SELECTOR, '.CircleButton.CircleButton_type_prev')
    CURRENT_IMAGE = (By.CSS_SELECTOR, '.MMImage-Preview')

