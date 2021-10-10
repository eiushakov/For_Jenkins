import pytest
from selenium import webdriver


@pytest.fixture()
def browser():
    browser = webdriver.Chrome(executable_path="//usr//local//bin//chromedriver")
    yield browser
    browser.quit()
