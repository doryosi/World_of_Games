from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import os


# Grabbing the chromedriver in order to do tests
def safe_cast(val, to_type, default=int):
    try:
        return to_type(val)
    except (ValueError, TypeError):
        return default


def test_scores_service():
    my_driver = webdriver.Chrome(executable_path="/bin/chromedriver")
    my_driver.get("http://127.0.0.1:5003/")
    wait = WebDriverWait(my_driver, 20)
    score = int(wait.until(EC.visibility_of_element_located((By.ID, "score"))).text)
    if 1000 >= score >= 1:
        return True
    else:
        return False


def main_functions():
    test_scores_service()
    if not test_scores_service():
        exit(-1)
    else:
        exit(0)


print(main_functions())
