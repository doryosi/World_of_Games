from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common import action_chains
from selenium.webdriver.chrome.webdriver import ChromiumDriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import common
import MainScore
import sys


def test():
    # MainScore.start_server()
    serv_obj = Service("C:/chromedriver")
    my_driver = webdriver.Chrome(executable_path="C:/chromedriver")
    # my_driver = webdriver.Chrome(service=serv_obj)
    url = "http://127.0.0.1:5003/"
    my_driver.get(url)
    result = my_driver.find_element_by_xpath("/html/body/h1").text
    my_driver.close()
    return result


x = test()
print(x)


