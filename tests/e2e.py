from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from Utils import bad_return_code, success_return_code

DEFAULT_FLASK_APP_URL = "http://127.0.0.1:5003/"
BIN_CHROME_DRIVER_DEST = "/usr/local/bin"


def test_scores_service():
    try:
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        full_bin_path = ChromeDriverManager(path=BIN_CHROME_DRIVER_DEST).install()
        my_driver = webdriver.Chrome(service=ChromeService(full_bin_path), options=chrome_options)
        my_driver.get(DEFAULT_FLASK_APP_URL)
        score = my_driver.find_element(by="xpath", value='//*[@id="score"]').text
        print(score)
        my_driver.close()
        return int(score) in range(1, 1001)
    except ValueError as e:
        print(e)
        return False


def main_function():
    if test_scores_service():
        return success_return_code
    else:
        print("Score is not in range...")
        return bad_return_code


main_function()
