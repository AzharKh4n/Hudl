from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
s = Service('/Users/khan/PycharmProjects/Hudl/chromedriver')


class TestNonFunctional:
    driver = ''
    baseURL = 'https://www.hudl.com/login'

    def test_remember_me(self):
        self.driver = webdriver.Chrome(service=s)
        self.driver.implicitly_wait(5)
        self.driver.get(self.baseURL)
        email = self.driver.find_element(By.ID, 'email')
        email.send_keys('ioptimise@gmail.com')
        password = self.driver.find_element(By.ID, 'password')
        password.send_keys('fOxgate82')
        checkbox = self.driver.find_element(By.CLASS_NAME, 'uni-form__check-indicator__background')
        checkbox.click()
        login = self.driver.find_element(By.ID, 'logIn')
        login.click()
        WebDriverWait(self.driver, 5).until(EC.title_is('Home - Hudl'))
        self.driver.close()
        self.driver = webdriver.Chrome(service=s)
        self.driver.implicitly_wait(5)
        self.driver.get('https://www.hudl.com/home')

    def test_password_asterisks(self):
        self.driver = webdriver.Chrome(service=s)
        self.driver.implicitly_wait(5)
        self.driver.get(self.baseURL)
        check_pass = self.driver.find_element(By.XPATH, "//*[@type='password']")
        assert check_pass.is_displayed()
        self.driver.quit()

    def test_logout_session(self):
        self.driver = webdriver.Chrome(service=s)
        self.driver.implicitly_wait(5)
        self.driver.get(self.baseURL)
        email = self.driver.find_element(By.ID, 'email')
        email.send_keys('ioptimise@gmail.com')
        password = self.driver.find_element(By.ID, 'password')
        password.send_keys('fOxgate82')
        checkbox = self.driver.find_element(By.CLASS_NAME, 'uni-form__check-indicator__background')
        checkbox.click()
        login = self.driver.find_element(By.ID, 'logIn')
        login.click()
        WebDriverWait(self.driver, 5).until(EC.title_is('Home - Hudl'))
        expand_menu = self.driver.find_element(By.CSS_SELECTOR, '.hui-globaluseritem__display-name')
        expand_menu.click()
        logout = self.driver.find_element(By.CSS_SELECTOR, "[data-qa-id='webnav-usermenu-logout']")
        logout.click()
        self.driver.back()
        actual_title = self.driver.title
        if actual_title == 'Log In':
            assert True
        else:
            print(actual_title)
            assert False
        self.driver.quit()
