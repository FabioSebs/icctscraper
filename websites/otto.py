from setup import WebScraper
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
import re


class OttoScraper(WebScraper):
    def perform_scraping(self):
        # wait for site to load
        # Set initial scroll position and increment
        scroll_position = 0
        scroll_increment = 1000  # Adjust as needed

        while True:
            # Scroll down by the increment
            self.driver.execute_script(f"window.scrollBy(0, {scroll_increment});")
            scroll_position += scroll_increment

            # Wait briefly for content to load
            time.sleep(2)

            # Check if we've reached the bottom of the page
            if scroll_position >= self.driver.execute_script("return document.body.scrollHeight"):
                break
        


        evs = self.driver.find_elements(
            By.CSS_SELECTOR, 'main.listing div.container div.col-2 ul.d-flex.flex-wrap.listing-card-wrap li.card div.card-panel'
        )

        for ev in evs:
            try:
                
                result_data = {
                    "Model": ev.find_element(By.CSS_SELECTOR,"a").text,  
                    "Price": ev.find_element(By.CSS_SELECTOR,"div.vh-price").text,
                    "Year": "",
                    "Acceleration": "",
                    "Top-Speed": "",
                    "Range": "",
                    "Efficiency": "",
                    "Fast-Charge": ""
                }

                print(result_data)

                self.entries.append(result_data)
            except Exception as e:
                print(e)
                continue

        # creating json record
        

        self.driver.quit()
