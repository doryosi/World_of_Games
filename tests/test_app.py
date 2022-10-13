from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdrivermanager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService


# Grabbing the chromedriver in order to do tests
def safe_cast(val, to_type, default=int):
    try:
        return to_type(val)
    except (ValueError, TypeError):
        return default


def test_scores_service():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().download_and_install()))
    driver = webdriver.Chrome(executable_path="C:/chromedriver")
    driver.get("http://127.0.0.1:5003")
    wait = WebDriverWait(driver, 20)
    score = int(wait.until(EC.visibility_of_element_located((By.ID, "score"))).text)
    if 1000 >= score >= 1:
        return exit(0)
    else:
        return exit(-1)


test_scores_service()


