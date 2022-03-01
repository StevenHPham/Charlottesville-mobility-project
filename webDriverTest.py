from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions

def test_driver_manager_chrome():
    service = ChromeService(executable_path=ChromeDriverManager().install())

    driver = webdriver.Chrome(service=service)

    driver.quit()


def test_chrome_session():
    options = ChromeOptions()

    driver = webdriver.Chrome(options=options,executable_path="/Users/stevenpham/.wdm/drivers/chromedriver/mac64/98.0.4758.102")

    driver.quit()








#test_driver_manager_chrome()

#Driver has been saved in cache /Users/stevenpham/.wdm/drivers/chromedriver/mac64/98.0.4758.102


test_chrome_session()



