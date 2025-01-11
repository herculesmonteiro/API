from selenium import webdriver
from utils.api_client import APIClient

def before_all(context):
    context.api_client = APIClient("https://demoqa.com")

def before_scenario(context, scenario):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()

def after_scenario(context, scenario):
    context.driver.quit()
