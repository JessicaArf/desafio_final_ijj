from selenium.webdriver.common.by import By
from utils.logger_config import logger
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, WebDriverException


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

        self.email_input_locator = (By.NAME, "email")
        self.password_input_locator = (By.NAME, "password")
        self.submit_button_locator = (By.CSS_SELECTOR, ".sc-eqUAAy.dFhnRi")
        self.login_label_locator = (By.XPATH, "//label[text()='Faça login']")

    def _wait(self, locator, timeout=10, condition=EC.presence_of_element_located):
        try:
            return WebDriverWait(self.driver, timeout).until(condition(locator))
        except TimeoutException as e:
            logger.error(f"Timeout ao esperar pelo elemento com locator: {locator}. Erro: {str(e)}")
            raise 
        except NoSuchElementException as e:
            logger.error(f"Elemento não encontrado com o locator: {locator}. Erro: {str(e)}")
            raise 
        except WebDriverException as e:
            logger.error(f"Erro no WebDriver ao tentar localizar o elemento com locator: {locator}. Erro: {str(e)}")
            raise  

    def wait_and_click(self, locator):
        try:
            logger.info(f"Clicando no elemento localizado: {locator}")
            element = self._wait(locator, condition=EC.element_to_be_clickable)  # Espera pelo elemento ser clicável
            element.click()
        except Exception as e:
            logger.error(f"Erro ao tentar clicar no elemento com locator: {locator}. Erro: {str(e)}")
            raise 

    def fill_email(self, email):
        try:
            logger.info(f"Preenchendo o email do login com: {email}")
            email_input = self._wait(self.email_input_locator)
            email_input.send_keys(email)
        except Exception as e:
            logger.error(f"Erro ao preencher o email com: {email}. Erro: {str(e)}")
            raise  

    def fill_password(self, password):
        try:
            logger.info("Preenchendo a senha do login")
            password_input = self._wait(self.password_input_locator)
            password_input.send_keys(password)
        except Exception as e:
            logger.error(f"Erro ao preencher a senha. Erro: {str(e)}")
            raise  

    def submit(self):
        try:
            logger.info("Clicando no botão iniciar sessão")
            self.wait_and_click(self.submit_button_locator)
        except Exception as e:
            logger.error(f"Erro ao submeter o formulário de login. Erro: {str(e)}")
            raise  

    def verify_login_failed(self):
      
        try:
             logger.info("Verificando se continua na página de login")
             login_label = self._wait(self.login_label_locator)
             actual = login_label.text
             assert "Faça login" in actual, (
             f"Esperado: 'Faça login', mas foi: '{actual}'"
              )
        except Exception as e:
            logger.error(f"Erro ao verificar falha no login: {e}")
            raise