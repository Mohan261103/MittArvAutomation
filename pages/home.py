from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Home:
    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)

        self.title_image = '//nav/img'
        self.add_contact_button = '//button'
        self.contact_name = "//input[@placeholder='John Doe']"
        self.contact_email = "//input[@placeholder='jane-doe@example.com']"
        self.next_button = "//button[normalize-space()='Next']"
        self.country_dropdown = "//div[@class='DD15__Container']//img"
        self.search_country = "//div[@class='search-inp']/input"
        self.country_india = '(//div[@class="dropdown__text"])[2]'
        self.phone_no = "//input[@placeholder='0000000000']"
        self.relation_dropdown = "(//div[@class='dropdown_text'])[2]/img"
        self.relation_parent = "//p[normalize-space()='Parent']"
        self.shortlist = "(//input[@type='checkbox'])[1]"
        self.done_button = "//button[normalize-space()='Done']"

        self.create_will = "//p[contains(text(),'Create a')]"
        self.text_will = "//p[normalize-space()='New Text Will']"
        self.click_for_dropdown = "//img[@alt='weg']"
        self.search_contact =  "//input[@placeholder='Search for a contact by name']"
        self.select_contact =  "//div[contains(@class,'connections_list')]//div[1]"
        self.subject = "//input[@class='subject_input_field']"
        self.delivery_dropdown =  "//div[@class='selected_deliver']//img"
        self.delivery_Posthumously = "(//p[@class='t105'])[1]"
        self.text_box = "//div[contains(@data-placeholder,'Preserve memories, pen wisdom, leave a written legacy that lasts forever')]"
        self.save_will = "//button[normalize-space()='Save Emotional Will']"


    def wait_until_main_page_loaded(self):
        self.wait.until(expected_conditions.presence_of_element_located((By.XPATH,self.title_image)))

    def click_on_add_contacts(self):
        self.driver.find_element(By.XPATH,self.add_contact_button ).click()

    def add_contact_name_and_email(self,name,email):
        self.driver.find_element(By.XPATH,self.contact_name ).send_keys(name)
        self.driver.find_element(By.XPATH,self.contact_email ).send_keys(email)
        self.driver.find_element(By.XPATH,self.next_button).click()

    def add_phone_no(self,number):
        self.driver.find_element(By.XPATH,self.country_dropdown).click()
        self.wait.until(expected_conditions.presence_of_element_located((By.XPATH,self.search_country)))
        self.driver.find_element(By.XPATH,self.search_country).send_keys("India")
        self.driver.find_element(By.XPATH,self.country_india).click()
        self.driver.find_element(By.XPATH,self.phone_no).send_keys(number)

    def add_relation(self):
        self.driver.find_element(By.XPATH,self.relation_dropdown).click()
        self.driver.find_element(By.XPATH,self.relation_parent).click()

    def select_shortlist_contact(self):
        self.driver.find_element(By.XPATH,self.shortlist).click()

    def click_add_contact_done(self):
        self.driver.find_element(By.XPATH,self.done_button).click()



    def click_create_will_and_text_will(self):
        self.driver.find_element(By.XPATH,self.create_will).click()
        self.driver.find_element(By.XPATH,self.text_will).click()

    def add_for(self):
        self.driver.find_element(By.XPATH,self.click_for_dropdown).click()
        self.driver.find_element(By.XPATH,self.search_contact).send_keys("abc")
        self.driver.find_element(By.XPATH,self.select_contact).click()

    def add_subject(self,subject):
        self.driver.find_element(By.XPATH,self.subject).send_keys(subject)

    def add_delivery(self):
        self.driver.find_element(By.XPATH,self.delivery_dropdown).click()
        self.driver.find_element(By.XPATH,self.delivery_Posthumously).click()

    def add_text(self,text):
        self.driver.find_element(By.XPATH,self.text_box).send_keys(text)

    def click_save_emotional_will(self):
        self.driver.find_element(By.XPATH,self.save_will).click()