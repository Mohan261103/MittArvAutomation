import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Login:
    def __init__(self,driver):

        self.driver = driver
        self.wait = WebDriverWait(self.driver,20)

        self.google_icon = "//div[@class='login__socials']/img[contains(@src, 'google')]"
        self.google_username = "identifierId"
        self.username_next = '//*[@id="identifierNext"]/div/button/span'
        self.google_password = '//*[@id="password"]/div[1]/div/div[1]/input'
        self.password_next = '//*[@id="passwordNext"]/div/button/span'
        self.google_continue = '//*[@id="yDmH0d"]/c-wiz/div/div[3]/div/div/div[2]/div/div/button/span'
        self.title_image = '//nav/img'
        self.login_title = "//h2"

    def verify_login_title(self):
        assert "Sign in" in self.driver.find_element(By.XPATH,self.login_title).text

    def wait_until_login_page_is_loaded(self):
        self.wait.until(expected_conditions.presence_of_element_located((By.XPATH,self.google_icon)))

    def check_no_of_windows(self,no):
        assert len(self.driver.window_handles) == 1

    def click_on_google_icon(self):
        time.sleep(5)
        self.driver.find_element(By.XPATH, self.google_icon).click()

    def switch_to_window(self,v):
        handles = []
        if v == 1:
            self.wait.until(expected_conditions.number_of_windows_to_be(2))
            handles = self.driver.window_handles
            newHandle = handles[1]
            self.driver.switch_to.window(newHandle)
        elif v == 0:
            self.wait.until(expected_conditions.number_of_windows_to_be(1))
            # self.driver.switch_to.default_content()
            self.driver.switch_to.window(self.driver.window_handles[0])


    def login_to_google(self):

        self.driver.find_element(By.ID, self.google_username ).send_keys("tqmohan@gmail.com")
        self.driver.find_element(By.XPATH, self.username_next).click()
        self.driver.find_element(By.XPATH,self.google_password ).send_keys("#Tqmohan26")
        self.driver.find_element(By.XPATH, self.password_next).click()
        self.driver.find_element(By.XPATH, self.google_continue ).click()

