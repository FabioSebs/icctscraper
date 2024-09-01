from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import json

class WebScraper:
    def __init__(self, url, fname) -> None:
        self.url = url  # URL to scrape
        self.fname = fname  # Output file name

        # Setup Chrome options
        chrome_options = Options()

        # If you want to use a specific Chrome binary
        chrome_options.binary_location = "./chromedriver"

        # Initialize the Chrome WebDriver using WebDriverManager
        self.driver = webdriver.Chrome(options=chrome_options)
        self.entries = []

    def navigate_to_url(self):
        self.driver.get(self.url)

    # NOTE: Override this method in subclasses to perform specific scraping
    def perform_scraping(self):
        pass

    def write_json(self):
        with open(self.fname, "w") as json_file:
            json.dump(self.entries, json_file, indent=2)

    def append_entry(self, new_entry):
        self.entries.append(new_entry)
        self.write_json()

    def close_driver(self):
        if self.driver:
            self.driver.quit()

    def run(self):
        try:
            self.navigate_to_url()
            self.perform_scraping()
            self.write_json()
        finally:
            self.close_driver()
