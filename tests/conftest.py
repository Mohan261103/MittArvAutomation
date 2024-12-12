from selenium import webdriver
import pytest

@pytest.fixture(scope= "class")
def setup_local(request):
    global driver
    driver = webdriver.Chrome()
    driver.implicitly_wait(30)
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.quit()
