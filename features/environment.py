from selenium import webdriver
from faker import Faker
from dotenv import load_dotenv
import os

load_dotenv()

def before_all(context):
   context.fake = Faker()
   os.environ['VALID_EMAIL_REGISTER'] = context.fake.email()
   
def before_scenario(context, scenario):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.get("https://projetofinal.jogajuntoinstituto.org/")
    

def after_scenario(context, scenario):
  context.driver.quit()