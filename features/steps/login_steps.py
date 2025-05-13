from behave import given, when, then
from selenium import webdriver
from pages.login_page import LoginPage
import time


@given("que o usuário está na página de login")
def step_impl(context):
    context.login_page = LoginPage(context.driver)

@when("ele preenche o e-mail e a senha válidos")
def step_impl(context):
    context.login_page.fill_email("jessica@email.com")
    context.login_page.fill_password("123456")

@when("ele preenche e-mail e senha inválidos")
def step_impl(context):
    context.login_page.fill_email("errado@teste.com")
    context.login_page.fill_password("errada")

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
    