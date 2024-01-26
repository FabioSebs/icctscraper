from setup import WebScraper
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time
import re 

class TripAdvisorScraper(WebScraper):
    def perform_scraping(self):
        # eait for site to load
        time.sleep(5)
        for i in range(1, 35):
            # div.ui_columns
            parent_elements = self.driver.find_elements(
                By.CSS_SELECTOR, "div.ui_columns div.prw_rup div div.main_content div.search-results-list div.ui_columns div.ui_column div.ui_columns"
            )

            for parent_element in parent_elements:
                try:
                
                    title = parent_element.find_element(
                        By.CSS_SELECTOR, "div.ui_column div.prw_rup div.result div.ui_columns div.ui_column.is-9-desktop div.location-meta-block div.result-title span"
                    ).text.strip()

                    location = parent_element.find_element(
                        By.CSS_SELECTOR, "div.ui_column div.prw_rup div.result div.ui_columns div.ui_column.is-9-desktop div.location-meta-block div.address div.address-text"
                    ).text.strip()

                    rating = parent_element.find_element(
                        By.CSS_SELECTOR, "div.ui_column div.prw_rup div.result div.ui_columns div.ui_column.is-9-desktop div.location-meta-block div.rating-review-count div.prw_rup span.ui_bubble_rating"
                    ).get_attribute("alt")

                    review_no = parent_element.find_element(
                        By.CSS_SELECTOR, "div.ui_column div.prw_rup div.result div.ui_columns div.ui_column.is-9-desktop div.location-meta-block div.rating-review-count div.prw_rup a"
                    ).text.strip()

                    source = parent_element.find_element(
                        By.CSS_SELECTOR, "div.ui_column div.prw_rup div.result div.ui_columns div.ui_column.is-9-desktop div.location-meta-block div.result-title"
                    ).get_attribute("onClick")
                    pattern = r"'/Attraction_Review[^']*\.html'"
                    match = re.search(pattern, source)

                    if match:
                        source = match.group(0)
                    
                    # creating json record
                    result_data = {
                        "Title": title,
                        "Location": location,
                        "Address": location,
                        "PostCode": "",
                        "Review": rating,
                        "ReviewNumber": review_no,
                        "Price": "-",
                        "Source": source
                    }

                    self.entries.append(result_data)
                    self.append_entry(result_data)

                except Exception as e:
                    continue

            # next button
            if i == 34:
                break

            next_button = self.driver.find_element(By.XPATH, "//a[contains(text(), 'Next')]")
            next_button.click()
            time.sleep(5)
