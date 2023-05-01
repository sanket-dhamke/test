'''
login to google
amazon
search samsung phone rabge 5000-20000
display list
'''
import pytest
import webdriver_manager
from selenium import webdriver
from selenium.webdriver.common.actions import action_builder
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import wait


class TestAmazon:
    def __int__(self):
        print("Hi")

    def test_amazon(self):
        self.driver = webdriver.Chrome(ChromeDriverManager.install())
        self.driver.get("https://www.google.com/")
        self.driver.find_element(By.ID, "//*[@id='APjFqb'']").click()
        self.driver.find_element(By.ID, "//*[@id='APjFqb'']").send_keys("Amazon")

        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//h3[text(),'Amazon.in'")))
        element.click()

        self.driver.quit()





a1 = TestAmazon()
a1.test_amazon()
