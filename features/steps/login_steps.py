from behave import given, when, then
from selenium import webdriver
from pages.login_page import LoginPage
import time
import os
from dotenv import load_dotenv


load_dotenv()

@given("que o usuário está na página de login")
def step_impl(context):
    context.login_page = LoginPage(context.driver)

@when("ele preenche o campo e-mail")
def step_impl(context):
    context.login_page.fill_email(os.getenv("VALID_EMAIL_LOGIN"))

@when("ele preenche o campo senha")
def step_impl(context):    
    context.login_page.fill_password(os.getenv("VALID_PASSWORD_LOGIN"))

@when("ele preenche o e-mail inválido")
def step_impl(context):
    context.login_page.fill_email(os.getenv("INVALID_EMAIL_LOGIN"))

@when("ele preenche a senha inválida")
def step_impl(context):
    context.login_page.fill_password(os.getenv("INVALID_PASSWORD_LOGIN"))

@when("clica no botão de Iniciar sessão")
def step_impl(context):
    context.login_page.submit()

@then("ele deve ser redirecionado para a página inicial")
def step_impl(context):
    time.sleep(2)
    assert "products" in context.driver.current_url
    context.driver.quit()

@then("o sistema não deve realizar o login")
def step_impl(context):
   time.sleep(2)
   context.login_page.verify_login_failed()
   context.driver.quit()
    