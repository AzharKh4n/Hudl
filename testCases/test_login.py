import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig


class TestLogin:
    baseURL = ReadConfig.get_application_url()
    email = ReadConfig.get_email()
    password = ReadConfig.get_password()
    invalid_email = ReadConfig.get_invalid_email()
    unregistered_email = ReadConfig.get_unregistered_email()
    incorrect_password = ReadConfig.get_incorrect_password()

    def test_login(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.set_email(self.email)
        self.lp.set_password(self.password)
        self.lp.click_login()
        WebDriverWait(self.driver, 5).until(EC.title_is(ReadConfig.get_homepage_title()))
        actual_title = self.driver.title
        if actual_title == ReadConfig.get_homepage_title():
            assert True
        else:
            self.driver.save_screenshot("../Screenshots/test_login.png")
            assert False

    def test_login_enter(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.set_email(self.email)
        self.lp.password_return(self.password)
        WebDriverWait(self.driver, 5).until(EC.title_is(ReadConfig.get_homepage_title()))
        actual_title = self.driver.title
        if actual_title == ReadConfig.get_homepage_title():
            assert True
        else:
            self.driver.save_screenshot("../Screenshots/test_login_enter.png")
            assert False

    def test_logout(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.set_email(self.email)
        self.lp.set_password(self.password)
        self.lp.click_login()
        WebDriverWait(self.driver, 5).until(EC.title_is(ReadConfig.get_homepage_title()))
        self.lp.click_expand_menu()
        self.lp.click_logout()
        WebDriverWait(self.driver, 5).until(EC.title_is(ReadConfig.get_logged_out_title()))
        actual_title = self.driver.title
        if actual_title == ReadConfig.get_logged_out_title():
            assert True
        else:
            self.driver.save_screenshot("../Screenshots/test_logout.png")
            assert False

    def test_no_credentials(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.click_login()
        validation = self.lp.wait_org_validation()
        if validation == ["We didn't recognize that email and/or password.Need help?"]:
            assert True
        else:
            self.driver.save_screenshot("../Screenshots/test_no_credentials.png")
            assert False

    def test_invalid_email(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.set_email(self.invalid_email)
        self.lp.set_password(self.password)
        self.lp.click_login()
        validation = self.lp.wait_org_validation()
        if validation == ["We didn't recognize that email and/or password.Need help?"]:
            assert True
        else:
            self.driver.save_screenshot("../Screenshots/test_invalid_email.png")
            assert False

    def test_unregistered_email(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.set_email(self.unregistered_email)
        self.lp.set_password(self.password)
        self.lp.click_login()
        validation = self.lp.wait_org_validation()
        if validation == ["We didn't recognize that email and/or password.Need help?"]:
            assert True
        else:
            self.driver.save_screenshot("../Screenshots/test_unregistered_email.png")
            assert False

    def test_incorrect_password(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.set_email(self.email)
        self.lp.set_password(self.incorrect_password)
        self.lp.click_login()
        validation = self.lp.wait_org_validation()
        if validation == ["We didn't recognize that email and/or password.Need help?"]:
            assert True
        else:
            self.driver.save_screenshot("../Screenshots/test_incorrect_password.png")
            assert False

    def test_unregistered_org(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.link_org_login()
        WebDriverWait(self.driver, 5).until(EC.title_is(ReadConfig.get_org_login_title()))
        self.lp.set_org_email(self.email)
        self.lp.click_org_login()
        validation = self.lp.wait_org_validation()
        if validation == ['Enter the email address used for your organisation']:
            assert True
        else:
            self.driver.save_screenshot("../Screenshots/test_unregistered_org.png")
            assert False

    def test_unregistered_forgotten_password(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.click_help_link()
        WebDriverWait(self.driver, 5).until(EC.title_is(ReadConfig.get_help_title()))
        time.sleep(1)
        self.lp.set_help_email(self.unregistered_email)
        self.lp.click_reset_password()
        validation = self.lp.wait_validation_msg()
        if validation == ["That email address doesn't exist in Hudl. Check with your coach to ensure they have the "
                            "right email address for you."]:
            assert True
        else:
            self.driver.save_screenshot("../Screenshots/unregistered_forgotten_password.png")
            assert False

    def test_invalid_forgotten_password(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.set_email(self.invalid_email)
        self.lp.click_help_link()
        WebDriverWait(self.driver, 5).until(EC.title_is(ReadConfig.get_help_title()))
        time.sleep(1)
        self.lp.click_reset_password()
        validation = self.lp.wait_validation_msg()
        if validation == ["That isn't a valid email address. Make sure to use the email@domain.com format."]:
            assert True
        else:
            self.driver.save_screenshot("../Screenshots/invalid_forgotten_password.png")
            assert False

    def test_reset_password(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.set_email(self.email)
        self.lp.click_help_link()
        WebDriverWait(self.driver, 5).until(EC.title_is(ReadConfig.get_help_title()))
        time.sleep(1)
        self.lp.click_reset_password()
        confirmation = self.lp.wait_confirmation_msg()
        print(confirmation)
        if confirmation == ['Click the link in the email to reset your password.']:
            assert True
        else:
            self.driver.save_screenshot("../Screenshots/reset_password.png")
            assert False
