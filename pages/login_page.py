from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def fill_email(self, email):
        self.driver.find_element("name", "email").send_keys(email)

    def fill_password(self, password):
        self.driver.find_element("name", "password").send_keys(password)

    def submit(self):
        self.driver.find_element(By.CSS_SELECTOR, ".sc-eqUAAy.dFhnRi").click()

    def verify_login_failed(self):
        self.driver.find_element(By.XPATH, "//label[text()='Faça login']")    