from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

class RegisterProductsPage:
    def __init__(self, driver):
        self.driver = driver

    def add_button(self):
        botao_adicionar = WebDriverWait(self.driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Adicionar')]"))
       )
        botao_adicionar.click()

    def fill_name_product(self, product):
       produto = self.driver.find_element(By.XPATH, "//input[@placeholder='Camiseta...']")
       produto.send_keys(product)

    def fill_description_product(self, description_product):
        self.driver.find_element("name", "description").send_keys(description_product)

    def select_category(self):
        self.driver.find_element(By.XPATH ,"//span[text()='Roupas']").click()

    def fill_price_product(self, price_product):
        self.driver.find_element("name", "price").send_keys(price_product)
    
    def upload_image_product(self, path_image):
        abs_path = os.path.abspath(path_image)
        input_file = self.driver.find_element(By.CSS_SELECTOR,'input[type="file"]')
        input_file.send_keys(abs_path)

    def fill_shipment_product(self, shipment_product):
        self.driver.find_element("name", "shipment").send_keys(shipment_product)   

    def submit(self):
        self.driver.find_element(By.CSS_SELECTOR,'button[type="submit"]').click()

    def verify_message_success(self):
        message_success = WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Produto enviado com sucesso')]"))
        )
        assert "Produto enviado com sucesso" in message_success.text, "Mensagem de sucesso não encontrada ou incorreta"
    
    def verify_error_message(self, expected_message):
        message = WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, f"//p[contains(text(), '{expected_message}')]"))
        )
        assert expected_message in message.text, f"Mensagem esperada: '{expected_message}' não foi exibida."



    

