from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.logger_config import logger
from selenium.common.exceptions import TimeoutException, NoSuchElementException, WebDriverException
import os


class RegisterProductsPage:
    def __init__(self, driver):
        self.driver = driver
        
        self.add_button_locator = (By.XPATH, "//button[contains(text(), 'Adicionar')]")
        self.name_input_locator = (By.XPATH, "//input[@placeholder='Camiseta...']")
        self.description_input_locator = (By.NAME, "description")
        self.category_locator = (By.XPATH, "//span[text()='Roupas']")
        self.price_input_locator = (By.NAME, "price")
        self.file_input_locator = (By.CSS_SELECTOR, 'input[type="file"]')
        self.shipment_input_locator = (By.NAME, "shipment")
        self.submit_button_locator = (By.CSS_SELECTOR, 'button[type="submit"]')
        self.success_message_locator = (By.XPATH, "//*[contains(text(), 'Produto enviado com sucesso')]")

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
            logger.error(f"Erro ao clicar no elemento com locator: {locator}. Erro: {str(e)}")
            raise

    def add_button(self):
        try:
            logger.info("Clicando no botão 'Adicionar'")
            self.wait_and_click(self.add_button_locator)
        except Exception as e:
            logger.error(f"Erro ao clicar no botão 'Adicionar': {str(e)}")
            raise

    def fill_name_product(self, product):
        try:
            logger.info(f"Preenchendo o campo 'Nome do produto' com: {product}")
            input_name = self._wait(self.name_input_locator)
            input_name.send_keys(product)
        except Exception as e:
            logger.error(f"Erro ao preencher o campo 'Nome do produto': {str(e)}")
            raise

    def fill_description_product(self, description_product):
        try:
            logger.info("Preenchendo o campo 'Descrição do produto'")
            input_description = self._wait(self.description_input_locator)
            input_description.send_keys(description_product)
        except Exception as e:
            logger.error(f"Erro ao preencher o campo 'Descrição do produto': {str(e)}")
            raise

    def select_category(self):
        try:
            logger.info("Selecionando a categoria 'Roupas'")
            self.wait_and_click(self.category_locator)
        except Exception as e:
            logger.error(f"Erro ao selecionar a categoria 'Roupas': {str(e)}")
            raise

    def fill_price_product(self, price_product):
        try:
            logger.info(f"Preenchendo o campo 'Preço do produto' com: {price_product}")
            input_price = self._wait(self.price_input_locator)
            input_price.send_keys(price_product)
        except Exception as e:
            logger.error(f"Erro ao preencher o campo 'Preço do produto': {str(e)}")
            raise

    def upload_image_product(self, path_image):
        try:
            logger.info("Fazendo upload da imagem do produto")
            abs_path = os.path.abspath(path_image)
            input_file = self._wait(self.file_input_locator)
            input_file.send_keys(abs_path)
        except Exception as e:
            logger.error(f"Erro ao fazer upload da imagem: {str(e)}")
            raise

    def fill_shipment_product(self, shipment_product):
        try:
            logger.info(f"Preenchendo o campo 'Frete do produto' com: {shipment_product}")
            input_shipment = self._wait(self.shipment_input_locator)
            input_shipment.send_keys(shipment_product)
        except Exception as e:
            logger.error(f"Erro ao preencher o campo 'Frete do produto': {str(e)}")
            raise

    def submit(self):
        try:
            logger.info("Clicando no botão 'Enviar Novo Produto'")
            self.wait_and_click(self.submit_button_locator)
        except Exception as e:
            logger.error(f"Erro ao clicar no botão de envio do produto: {str(e)}")
            raise

    def verify_message_success(self):
        try:
            logger.info("Verificando mensagem de sucesso do produto cadastrado")
            message_success = self._wait(self.success_message_locator)
            actual = message_success.text
            assert "Produto enviado com sucesso" in actual, (
                f"Esperado: 'Produto enviado com sucesso', mas foi: '{actual}'"
            )
        except Exception as e:
            logger.error(f"Erro ao verificar mensagem de sucesso: {str(e)}")
            raise

    def verify_error_message(self, expected_message):
        try:
            logger.info(f"Verificando mensagem de erro esperada: '{expected_message}'")
            message = self._wait((By.XPATH, f"//p[contains(text(), '{expected_message}')]"))
            actual = message.text
            assert expected_message in actual, (
                f"Mensagem esperada: '{expected_message}', mas foi: '{actual}'"
            )
        except Exception as e:
            logger.error(f"Erro ao verificar mensagem de erro: {str(e)}")
            raise
    

