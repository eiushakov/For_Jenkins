import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@allure.feature('Start browser')
@pytest.fixture()
def browser():
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    browser = webdriver.Chrome(options=options)
    yield browser
    browser.quit()
