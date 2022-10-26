from selenium.webdriver.chrome.service import Service
from selenium import webdriver
import pytest


@pytest.fixture()
def setup():
    s = Service('/Users/khan/PycharmProjects/Hudl/chromedriver')
    driver = webdriver.Chrome(service=s)
    driver.maximize_window()
    yield driver
    driver.close()
