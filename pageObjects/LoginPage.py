from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    textbox_email_id = "email"
    textbox_password_id = "password"
    button_login_id = "logIn"
    button_expand_css_selector = ".hui-globaluseritem__display-name"
    button_logout_css_selector = "[data-qa-id='webnav-usermenu-logout']"
    link_org_login_xpath = "//button[normalize-space()='Log In with an Organization']"
    textbox_org_email_id = "uniId_1"
    button_org_login_xpath = "//button[normalize-space()='Log In']"
    text_org_validation_xpath = "//p[@class='uni-text']"
    link_help_xpath = "//a[normalize-space()='Need help?']"
    textbox_help_email_xpath = "//input[@type='text']"
    button_reset_password_tag_name = "button"
    text_reset_pwd_confirmation_xpath = "//p[contains(text(),'Click the link in the email to reset your password')]"

    def __init__(self, driver):
        self.driver = driver

    def set_email(self, email):
        self.driver.find_element(By.ID, self.textbox_email_id).send_keys(email)

    def set_password(self, password):
        self.driver.find_element(By.ID, self.textbox_password_id).send_keys(password)

    def password_return(self, password):
        self.driver.find_element(By.ID, self.textbox_password_id).send_keys(password, Keys.ENTER)

    def click_login(self,):
        self.driver.find_element(By.ID, self.button_login_id).click()

    def click_expand_menu(self):
        self.driver.find_element(By.CSS_SELECTOR, self.button_expand_css_selector).click()

    def click_logout(self):
        self.driver.find_element(By.CSS_SELECTOR, self.button_logout_css_selector).click()

    def link_org_login(self):
        self.driver.find_element(By.XPATH, self.link_org_login_xpath).click()

    def set_org_email(self, email):
        self.driver.find_element(By.ID, self.textbox_org_email_id).send_keys(email)

    def click_org_login(self):
        self.driver.find_element(By.XPATH, self.button_org_login_xpath).click()

    def wait_validation_msg(self):
        return ([c.text for c in WebDriverWait(self.driver, 10).until(
            EC.visibility_of_all_elements_located((By.XPATH, self.text_org_validation_xpath)))])

    def wait_org_validation(self):
        return ([c.text for c in WebDriverWait(self.driver, 10).until(
            EC.visibility_of_all_elements_located((By.XPATH, self.text_org_validation_xpath)))])

    def click_help_link(self):
        self.driver.find_element(By.XPATH, self.link_help_xpath).click()

    def set_help_email(self, email):
        self.driver.find_element(By.XPATH, self.textbox_help_email_xpath).send_keys(email)

    def click_reset_password(self):
        self.driver.find_element(By.TAG_NAME, self.button_reset_password_tag_name).click()

    def wait_confirmation_msg(self):
        return ([c.text for c in WebDriverWait(self.driver, 10).until(
            EC.visibility_of_all_elements_located((By.XPATH, self.text_reset_pwd_confirmation_xpath)))])
