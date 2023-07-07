from pathlib import Path
from time import sleep
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

ROOT_DIR = Path(__file__).parent.parent
CHOMEDRIVER_NAME = 'chromedriver'
CHROMEDRIVER_PATH = ROOT_DIR / 'bin' / CHOMEDRIVER_NAME


def make_chrome_browser(*options):
    chrome_options = webdriver.ChromeOptions()

    if options is not None:
        for option in options:
            chrome_options.add_argument(option)
    
    if os.environ.get('SELENIUM_HEADLESS') == '1':
        chrome_options.add_argument('--headless')

    chrome_service = Service(executable_path=CHROMEDRIVER_PATH)
    browser = webdriver.Chrome(service=chrome_service, options=chrome_options)
    return browser


if __name__ == '__main__':
    browser = make_chrome_browser('--headless')
    browser.get('http://www.udemy.com/')
    sleep(5)
    browser.quit()