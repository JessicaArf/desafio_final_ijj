from behave import given, when, then
from pages.login_page import LoginPage
from pages.register_products_page import RegisterProductsPage
import os
from dotenv import load_dotenv


load_dotenv()

@given("que o usuário está logado")
def step_impl(context):
    context.register_products_page = RegisterProductsPage(context.driver)
    context.login_page = LoginPage(context.driver)
    context.login_page.fill_email(os.getenv("VALID_EMAIL_LOGIN"))
    context.login_page.fill_password(os.getenv("VALID_PASSWORD_LOGIN"))
    context.login_page.submit()

@given("clica no botão Adicionar")
def step_impl(context):
    context.register_products_page.add_button()

@when("preenche o nome do produto")
def step_impl(context):
    context.register_products_page.fill_name_product(os.getenv("NAME_PRODUCT")) 

@when("preenche a descrição do produto")       
def step_impl(context):
    context.register_products_page.fill_description_product(os.getenv("DESCRIPTION_PRODUCT")) 

@when("seleciona uma categoria")
def step_impl(context):
    context.register_products_page.select_category()  

@when("preenche o preço")
def step_impl(context):
    context.register_products_page.fill_price_product(os.getenv("PRICE_PRODUCT"))  

@when("faz o upload de uma imagem")
def step_impl(context):
    context.register_products_page.upload_image_product(os.getenv("PATH_IMAGE"))      

@when("preenche o frete")
def step_impl(context):
    context.register_products_page.fill_shipment_product(os.getenv("SHIPMENT_PRODUCT"))    

@when("clica no botão Enviar Novo Produto")
def step_impl(context):
    context.register_products_page.submit()    

@then("o produto deve ser cadastrado com sucesso")
def step_impl(context):
    context.register_products_page.verify_message_success()

