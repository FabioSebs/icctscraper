from setup import WebScraper
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time
import re 

class LACBScraper(WebScraper):
    def perform_scraping(self):
        # eait for site to load
        time.sleep(5)
        
        # div.ui_columns
        parent_elements = self.driver.find_elements(
            By.CSS_SELECTOR, "div.loc div#mntl-three-post__inner_1-0 a.mntl-card-list-items"
        )

        for parent_element in parent_elements:
            try:
                
                name = parent_element.find_element(
                    By.CSS_SELECTOR, "div.card__content span.card__title span.card__title-text"
                ).text.strip()

                image = parent_element.find_element(
                    By.CSS_SELECTOR, "div.loc div.card__media div.img-placeholder img"
                ).get_attribute("src")

                category = parent_element.find_element(
                    By.CSS_SELECTOR, "div.card__content"
                ).get_attribute("data-tag")

                url = parent_element.get_attribute("href")

                # creating json record
                result_data = {
                    "Name": name,
                    "Image": image,
                    "Category": category,
                    "URL": url,
                }

                self.entries.append(result_data)
                self.append_entry(result_data)

            except Exception as e:
                continue

