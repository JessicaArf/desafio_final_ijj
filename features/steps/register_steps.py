from behave import given, when, then
from selenium import webdriver
from pages.register_page import RegisterPage
import time
import os
from dotenv import load_dotenv


load_dotenv()

@given("que o usuário não possui conta e está na página de login")
def step_impl(context):
    context.register_page = RegisterPage(context.driver)

@when("ele clica no 'Clique aqui e registre-se'")
def step_impl(context):
    context.register_page.click_register_button()

@when("ele preenche o e-mail")
def step_impl(context):
    context.register_page.fill_email("testejessica19@email.com")

@when("ele preenche o e-mail sem @")
def step_impl(context):
    context.register_page.fill_email(os.getenv("INVALID_EMAIL_REGISTER"))  

@when("ele preenche a senha")
def step_impl(context):
    context.register_page.fill_password(os.getenv("CONFIRM_PASSWORD_REGISTER"))

@when("ele preenche o confirmar senha")    
def step_impl(context):
    context.register_page.fill_confirm_password(os.getenv("CONFIRM_PASSWORD_REGISTER"))
    
@when("ele preenche o confirmar senha com uma senha diferente")    
def step_impl(context):
    context.register_page.fill_confirm_password(os.getenv("WRONG_CONFIRM_PASSWORD_REGISTER")) 

@when("ele clica no botão de Criar conta")    
def step_impl(context):
    context.register_page.submit()

@then("uma mensagem de sucesso contendo 'Usuário cadastrado com sucesso' deve ser exibida")  
def step_impl(context):
    time.sleep(2)
    context.register_page.verify_message_success()

    
@then("uma mensagem de erro contendo 'Usuario ja existente com email informado' deve ser exibida")
def step_impl(context):
    context.register_page.verify_error_message_email()
  
@then("uma mensagem de erro contendo 'As senhas precisam ser iguais' deve ser exibida")
def step_impl(context):
    context.register_page.verify_error_message_password()

@then("uma mensagem de erro contendo 'Digite um e-mail válido' deve ser exibida")
def step_impl(context):
    context.register_page.verify_error_message_invalid_format_email()
     