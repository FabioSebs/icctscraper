from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

class WebScraper:
    def __init__(self, url) -> None:
        self.url = url
        self.driver = webdriver.Chrome()

    def navigate_to_url(self):
        self.driver.get(self.url)

    # NOTE: override this
    def perform_scraping(self):
        pass

    def close_driver(self):
        if self.driver:
            self.driver.quit()

    def run(self):
        try:
            self.navigate_to_url()
            time.sleep(5)
            self.perform_scraping()
        finally:
            self.close_driver()
