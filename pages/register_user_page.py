from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.logger_config import logger
from selenium.common.exceptions import TimeoutException, NoSuchElementException, WebDriverException


class RegisterPage:
    def __init__(self, driver):
        self.driver = driver

        self.register_button_locator = (By.CSS_SELECTOR, "span.register a")
        self.email_input_locator = (By.NAME, "email")
        self.password_input_locator = (By.NAME, "password")
        self.confirm_password_input_locator = (By.NAME, "confirmPassword")
        self.submit_button_locator = (By.CSS_SELECTOR, ".sc-dhKdcB.iFaZzk")
        self.success_message_locator = (By.CSS_SELECTOR, ".sucess")
        self.error_email_message_locator = (By.XPATH, "//span[text()='Usuario ja existente com email informado']")
        self.error_password_message_locator = (By.XPATH, "//span[text()='As senhas precisam ser iguais']")
        self.error_invalid_email_message_locator = (By.XPATH, "//p[text()='Digite um e-mail válido']")

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
            element = self._wait(locator, condition=EC.element_to_be_clickable)
            element.click()
        except Exception as e:
            logger.error(f"Erro ao clicar no elemento: {locator}. Erro: {str(e)}")
            raise

    def click_register_button(self):
        self.wait_and_click(self.register_button_locator)

    def fill_email(self, email):
        try:
            logger.info(f"Preenchendo o campo email com: '{email}'")
            email_input = self._wait(self.email_input_locator)
            email_input.send_keys(email)
        except Exception as e:
            logger.error(f"Erro ao preencher o email '{email}'. Erro: {str(e)}")
            raise

    def fill_password(self, password):
        try:
            logger.info("Preenchendo o campo senha")
            password_input = self._wait(self.password_input_locator)
            password_input.send_keys(password)
        except Exception as e:
            logger.error(f"Erro ao preencher a senha. Erro: {str(e)}")
            raise

    def fill_confirm_password(self, confirm_password):
        try:
            logger.info("Preenchendo o campo confirmar senha")
            confirm_password_input = self._wait(self.confirm_password_input_locator)
            confirm_password_input.send_keys(confirm_password)
        except Exception as e:
            logger.error(f"Erro ao preencher o campo confirmar senha. Erro: {str(e)}")
            raise

    def submit(self):
        try:
            logger.info("Clicando no botão Criar Conta")
            self.wait_and_click(self.submit_button_locator)
        except Exception as e:
            logger.error(f"Erro ao submeter o formulário de cadastro. Erro: {str(e)}")
            raise

    def verify_message_success(self):
        try:
            logger.info("Verificando mensagem de sucesso")
            message_success = self._wait(self.success_message_locator)
            actual = message_success.text
            assert "Usuário cadastrado com sucesso" in actual, (
                f"Esperado: 'Usuário cadastrado com sucesso', mas foi: '{actual}'"
            )
        except Exception as e:
            logger.error(f"Erro ao verificar mensagem de sucesso. Erro: {str(e)}")
            raise

    def verify_error_message_email(self):
        try:
            logger.info("Verificando mensagem de erro para e-mail existente")
            message_error = self._wait(self.error_email_message_locator)
            actual = message_error.text
            assert "Usuario ja existente com email informado" in actual, (
                f"Esperado: 'Usuario ja existente com email informado', mas foi: '{actual}'"
            )
        except Exception as e:
            logger.error(f"Erro ao verificar mensagem de erro do e-mail. Erro: {str(e)}")
            raise

    def verify_error_message_password(self):
        try:
            logger.info("Verificando mensagem de erro para senhas diferentes")
            message_error = self._wait(self.error_password_message_locator)
            actual = message_error.text
            assert "As senhas precisam ser iguais" in actual, (
                f"Esperado: 'As senhas precisam ser iguais', mas foi: '{actual}'"
            )
        except Exception as e:
            logger.error(f"Erro ao verificar mensagem de erro da senha. Erro: {str(e)}")
            raise

    def verify_error_message_invalid_format_email(self):
        try:
            logger.info("Verificando mensagem de erro de e-mail inválido")
            message_error = self._wait(self.error_invalid_email_message_locator)
            actual = message_error.text
            assert "Digite um e-mail válido" in actual, (
                f"Esperado: 'Digite um e-mail válido', mas foi: '{actual}'"
            )
        except Exception as e:
            logger.error(f"Erro ao verificar mensagem de e-mail inválido. Erro: {str(e)}")
            raise