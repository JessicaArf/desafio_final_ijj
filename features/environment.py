from selenium import webdriver
from faker import Faker
from dotenv import load_dotenv
import requests
import os

load_dotenv()

def before_all(context):
   context.fake = Faker()
   os.environ['VALID_EMAIL_REGISTER'] = context.fake.email()
   
def before_scenario(context, scenario):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.get(os.getenv("URL_WEB"))
    

def after_scenario(context, scenario):
  context.driver.quit()

def after_all(context):
    login_payload = {
        "email": os.getenv("VALID_EMAIL_LOGIN"),
        "password": os.getenv("VALID_PASSWORD_LOGIN")
    }

    login_response = requests.post(os.getenv("LOGIN_URL"), json=login_payload)

    if login_response.status_code == 200:
        response_data = login_response.json()
        token = response_data.get("token")

        headers = {
            "Authorization": f"Bearer {token}"
        }

        url_products = os.getenv("PRODUCTS_URL") 
        
        response_get_products = requests.get(url_products, headers=headers)

        if response_get_products.status_code == 200:
            products = response_get_products.json()

            for product in products:
                product_id = product.get("idprodutos")

                
                url_delete = f"{url_products}/{product_id}"  
                response_delete_products = requests.delete(url_delete, headers=headers)

                if response_delete_products.status_code == 200:
                    print(f"Produto {product_id} deletado com sucesso.")
                else:
                    print(f"Erro ao deletar o produto {product_id}: {response_delete_products.text}")
        else:
            print("Erro ao buscar produtos:", response_get_products.text)
    else:
        print("Erro ao fazer login:", login_response.text)