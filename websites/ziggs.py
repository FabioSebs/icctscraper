from setup import WebScraper
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
import re


class ZiggsScraper(WebScraper):
    def perform_scraping(self):
        # Loop until the "Load More" button is no longer visible
        while True:
            try:
                # Find the "Load More" button
                load_more_button = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, 'div.d-flex.justify-content-center a.btn-offer.mb-30')))
        
                # Click the button
                load_more_button.click()
        
                # Wait for some time to let the content load
                time.sleep(2)  # Adjust as needed
        
            except Exception as e:
                # If the button is no longer visible or clickable, exit the loop
                print("No more 'Load More' button.")
                break

        print("SCRAPING")
        time.sleep(4)

        rows = self.driver.find_elements(
            By.CSS_SELECTOR, '.new__car__column__lists.no-ssr-list .d-row'
        )

        for row in rows:
            items = row.find_elements(By.CSS_SELECTOR, ".col-md-12")
            for item in items:
                try:
                    result_data = {
                        "Model": item.find_element(By.CSS_SELECTOR, ".new__car__title").text.strip(),  
                        "Price": item.find_element(By.CSS_SELECTOR, ".new__car__price").text.strip(),
                        "Year": "",
                        "Acceleration": "",
                        "Top-Speed": "",
                        "Range": "",
                        "Efficiency": "",
                        "Fast-Charge": ""
                    }

                    self.entries.append(result_data)
                except Exception as e:
                    continue
        
        self.driver.quit()
