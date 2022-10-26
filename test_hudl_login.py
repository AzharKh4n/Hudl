from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestHudl:
    driver = ''
    baseURL = 'https://www.hudl.com/login'
    validation_message = ["We didn't recognize that email and/or password.Need help?"]
    org_validation_message = ['Enter the email address used for your organisation']
    reset_password_validation = ["That isn't a valid email address. Make sure to use the email@domain.com format."]
    user = {
        'EMAIL': 'ioptimise@gmail.com',
        'PASSWORD': 'fOxgate82'
    }
    invalid_user = {
        'EMAIL': 'QWERTY',
        'PASSWORD': 'PASSWORD'
    }
    non_hudl_user = {
        'EMAIL': 'johnsmith@gmail.com',
        'PASSWORD': 'fOxgate82'
    }

    def setup_method(self):
        # location of web driver
        s = Service('/Users/khan/PycharmProjects/Hudl/chromedriver')
        self.driver = webdriver.Chrome(service=s)
        self.driver.implicitly_wait(5)
        self.driver.get(self.baseURL)

    def test_successful_login(self):
        # login using valid credentials by clicking on the Log In button

        # find email field and enter email address
        email = self.driver.find_element(By.ID, 'email')
        email.send_keys(self.user['EMAIL'])

        # find password field and enter password
        password = self.driver.find_element(By.ID, 'password')
        password.send_keys(self.user['PASSWORD'])

        # find and click on log in button
        login = self.driver.find_element(By.ID, 'logIn')
        login.click()

        # wait for page to load & verify user has successfully logged in to homepage
        WebDriverWait(self.driver, 5).until(EC.title_is('Home - Hudl'))

        # verify user has successfully logged onto homepage via page title
        actual_title = self.driver.title
        if actual_title == 'Home - Hudl':
            assert True
        else:
            self.driver.save_screenshot("test_successful_login_enter.png")
            assert False

    def test_successful_login_enter(self):
        # login using valid credentials by pressing enter

        # find email field and enter email address
        email = self.driver.find_element(By.ID, 'email')
        email.send_keys(self.user['EMAIL'])

        # find password field and press the enter key
        password = self.driver.find_element(By.ID, 'password')
        password.send_keys(self.user['PASSWORD'], Keys.ENTER)

        # wait for homepage to load
        WebDriverWait(self.driver, 5).until(EC.title_is('Home - Hudl'))

        # verify user has successfully logged onto homepage via page title
        actual_title = self.driver.title
        if actual_title == 'Home - Hudl':
            assert True
        else:
            self.driver.save_screenshot("test_successful_login.png")
            assert False

    def test_logout(self):
        # login using valid credentials and clicking on the Log In button

        # find email field and enter email address
        email = self.driver.find_element(By.ID, 'email')
        email.send_keys(self.user['EMAIL'])

        # find password field and enter password
        password = self.driver.find_element(By.ID, 'password')
        password.send_keys(self.user['PASSWORD'])

        # find and click on login button
        login = self.driver.find_element(By.ID, 'logIn')
        login.click()

        # wait for page to load
        WebDriverWait(self.driver, 5).until(EC.title_is('Home - Hudl'))

        # find and click on menu to expand options
        expand_menu = self.driver.find_element(By.CSS_SELECTOR, '.hui-globaluseritem__display-name')
        expand_menu.click()

        # find and click on log out button
        logout = self.driver.find_element(By.CSS_SELECTOR, "[data-qa-id='webnav-usermenu-logout']")
        logout.click()

        # wait for page to load
        WebDriverWait(self.driver, 5).until(EC.title_is
                                            ('Hudl • Connected solutions for high-performance video and data analysis'))

        # verify user has successfully logged out via page title
        actual_title = self.driver.title
        if actual_title == 'Hudl • Connected solutions for high-performance video and data analysis':
            assert True
        else:
            self.driver.save_screenshot("test_logout.png")
            assert False

    def test_blank_credentials_login(self):
        # login without entering any credentials and clicking on the Log In button

        # find and click on log in button
        login = self.driver.find_element(By.ID, 'logIn')
        login.click()

        # find and store validation message
        validation = ([c.text for c in WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located
                                                                            ((By.XPATH, "//p[@class='uni-text']")))])

        # verify that the validation message is displayed
        if validation == self.validation_message:
            assert True
        else:
            self.driver.save_screenshot("test_blank_credentials_login.png")
            assert False

    def test_invalid_credentials_login(self):
        # attempt to login entering invalid credentials and click the Log In button

        # find email field & enter invalid format email address
        email = self.driver.find_element(By.ID, 'email')
        email.send_keys(self.invalid_user['EMAIL'])

        # find password field & enter password
        password = self.driver.find_element(By.ID, 'password')
        password.send_keys(self.invalid_user['PASSWORD'])

        # find & click on log in button
        login = self.driver.find_element(By.ID, 'logIn')
        login.click()

        # find and store validation message
        validation = ([c.text for c in WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located
                                                                            ((By.XPATH, "//p[@class='uni-text']")))])

        # verify that the validation message is displayed
        if validation == self.validation_message:
            assert True
        else:
            self.driver.save_screenshot("test_invalid_credentials_login.png")
            assert False

    def test_invalid_email_login(self):
        # attempt to login entering invalid email address and click the Log In button

        # find email field & enter unregistered user email address
        email = self.driver.find_element(By.ID, 'email')
        email.send_keys(self.non_hudl_user['EMAIL'])

        # find password field & enter password
        password = self.driver.find_element(By.ID, 'password')
        password.send_keys(self.non_hudl_user['PASSWORD'])

        # find & click on log in button
        login = self.driver.find_element(By.ID, 'logIn')
        login.click()

        # find and store validation message
        validation = ([c.text for c in WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located
                                                                            ((By.XPATH, "//p[@class='uni-text']")))])

        # verify that the validation message is displayed
        if validation == self.validation_message:
            assert True
        else:
            self.driver.save_screenshot("test_invalid_email_login.png")
            assert False

    def test_invalid_password_login(self):
        # attempt to login entering invalid password and click the Log In button

        # find email field & enter a valid registered email address
        email = self.driver.find_element(By.ID, 'email')
        email.send_keys(self.user['EMAIL'])

        # find password field & enter incorrect password
        password = self.driver.find_element(By.ID, 'password')
        password.send_keys(self.invalid_user['PASSWORD'])

        # find & click on log in button
        login = self.driver.find_element(By.ID, 'logIn')
        login.click()

        # find and store validation message
        validation = ([c.text for c in WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located
                                                                            ((By.XPATH, "//p[@class='uni-text']")))])

        # verify that the validation message is displayed
        if validation == self.validation_message:
            assert True
        else:
            self.driver.save_screenshot("test_invalid_password_login.png")
            assert False

    def test_invalid_organization_login(self):
        # attempt to login entering valid hudl single user credentials and click the Log In button

        # find & click on the log in via organization button
        org_login = self.driver.find_element(By.XPATH, "//button[normalize-space()='Log In with an Organization']")
        org_login.click()

        # wait for page to load
        WebDriverWait(self.driver, 5).until(EC.title_is('Log In with Organization - Hudl'))

        # find email field & enter registered personal email address
        email = self.driver.find_element(By.ID, 'uniId_1')
        email.send_keys(self.user['EMAIL'])

        # find & click on log in button
        login_org = self.driver.find_element(By.XPATH, "//button[normalize-space()='Log In']")
        login_org.click()

        # find and store validation message
        validation = ([c.text for c in WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located
                                                                            ((By.XPATH, "//p[@class='uni-text']")))])

        # verify that the validation message is displayed
        if validation == self.org_validation_message:
            assert True
        else:
            self.driver.save_screenshot("test_invalid_organization_login.png")
            assert False

    def test_forgotten_password(self):
        # attempt to reset password using an invalid email address

        # find & click on the need help button
        need_help = self.driver.find_element(By.XPATH, "//a[normalize-space()='Need help?']")
        need_help.click()

        # wait for page to load
        WebDriverWait(self.driver, 5).until(EC.title_is('Log In'))

        # find email field & enter an email with an invalid format
        email = self.driver.find_element(By.CLASS_NAME, 'styles_loginInput_3jFnWKYDKHd3thsrh95xCu')
        email.send_keys(self.invalid_user['EMAIL'])

        # find & click on the reset password button
        reset_password = self.driver.find_element(By.TAG_NAME, "button")
        reset_password.click()

        # find and store validation message
        validation = ([c.text for c in WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located
                                                                            ((By.XPATH, "//p[@class='uni-text']")))])

        # verify that the validation message is displayed
        if validation == self.reset_password_validation:
            assert True
        else:
            self.driver.save_screenshot("test_forgotten_password.png")
            assert False

    def test_reset_password(self):
        # reset password using a valid email address

        # find & click on the need help button
        need_help = self.driver.find_element(By.XPATH, "//a[normalize-space()='Need help?']")
        need_help.click()

        # wait for page to load
        WebDriverWait(self.driver, 5).until(EC.title_is('Log In'))

        # find email field & enter registered personal email address
        email = self.driver.find_element(By.CLASS_NAME, 'styles_loginInput_3jFnWKYDKHd3thsrh95xCu')
        email.send_keys(self.non_hudl_user['EMAIL'])

        # find & click on reset password button
        reset_password = self.driver.find_element(By.TAG_NAME, "button")
        reset_password.click()

        # find and store confirmation message
        confirmation = self.driver.find_element(By.XPATH, "//h3[normalize-space()='Check Your Email']").get_attribute('innerHTML')

        # verify that the confirmation message is displayed
        if confirmation == 'Check Your Email':
            assert True
        else:
            self.driver.save_screenshot("test_reset_password.png")
            assert False

    def teardown_method(self):
        self.driver.quit()
