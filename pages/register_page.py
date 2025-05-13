from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class RegisterPage:
    def __init__(self, driver):
        self.driver = driver

    def click_register_button(self):
        self.driver.find_element(By.CSS_SELECTOR, "span.register a").click()

    def fill_email(self, email):
        self.driver.find_element("name", "email").send_keys(email)

    def fill_password(self, password):
        self.driver.find_element("name", "password").send_keys(password)

    def fill_confirm_password(self, confirm_password):   
        self.driver.find_element("name", "confirmPassword").send_keys(confirm_password)

    def submit(self):
        self.driver.find_element(By.CSS_SELECTOR, ".sc-dhKdcB.iFaZzk").click()    
  

    def verify_message_success(self):
        message_success = self.driver.find_element(By.CSS_SELECTOR, ".sucess")
        assert "Usuário cadastrado com sucesso" in message_success.text, "Mensagem de sucesso não encontrada ou incorreta"

    def verify_error_message_email(self):
        message_error = WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[text()='Usuario ja existente com email informado']"))
        )
        assert "Usuario ja existente com email informado" in message_error.text, "Mensagem de erro não encontrada ou incorreta"

    def verify_error_message_password(self):
        message_error = WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[text()='As senhas precisam ser iguais']"))
        )
        assert "As senhas precisam ser iguais" in message_error.text, "Mensagem de erro não encontrada ou incorreta"   


  