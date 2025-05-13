from selenium import webdriver
import requests

def before_scenario(context, scenario):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.get("https://projetofinal.jogajuntoinstituto.org/")

def after_scenario(context, scenario):
  context.driver.quit()