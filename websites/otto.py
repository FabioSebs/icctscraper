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
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'main#main-content')))

               # Get initial height of the page
        last_height = self.driver.execute_script(
            "return document.body.scrollHeight")

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

        # Now parse the items
        # Example: Extract text from all elements with a specific class
        evs = self.driver.find_elements(
            By.CSS_SELECTOR, 'section.css-t6ry6e.ed8c72418 section.css-1xl6iji.efx9mrk10 div.css-q242xx.efx9mrk9 div.listicle-slides.css-ducv57.eafkxkw0 div.css-189pu4y.efx9mrk8 h2.css-rxobiv.efx9mrk7'
        )

        evs2 = self.driver.find_elements(
            By.CSS_SELECTOR, 'section.css-t6ry6e.ed8c72418 section.css-1xl6iji.efx9mrk10 div.css-q242xx.efx9mrk9 div.listicle-slides.css-ducv57.eafkxkw0 div.css-189pu4y.efx9mrk8 h2.css-155wfso.efx9mrk7'
        )
        

        for ev in evs:
            try:
                 print(ev.text.strip())
            except Exception as e:
                continue
        
        for ev in evs2:
            try:
                 print(ev.text.strip())
            except Exception as e:
                continue
        # Close the browser
        self.driver.quit()
