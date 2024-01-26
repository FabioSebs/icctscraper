from setup import WebScraper
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time
import re 

class BookingsScraper(WebScraper):
    def perform_scraping(self):
        # eait for site to load
        time.sleep(5)
        for i in range(1, 41):
            # div.ui_columns
            parent_elements = self.driver.find_elements(
                By.CSS_SELECTOR, "div.df7e6ba27d div.bcbf33c5c3 div.dcf496a7b9 div.d4924c9e74"
            )

            for parent_element in parent_elements:
                try:
                    title = parent_element.find_element(
                        By.CSS_SELECTOR, "div.c82435a4b8 div.c066246e13 div.c1edfbabcb div.aca0ade214 div.aaee4e7cd3 div.aca0ade214 div.d6767e681c h3 a div"
                    ).text.strip()

                    location = parent_element.find_element(
                        By.CSS_SELECTOR, "div.c82435a4b8 div.c066246e13 div.c1edfbabcb div.aca0ade214 div.aaee4e7cd3 div.aca0ade214 div a span span.aee5343fdb.def9bc142a"
                    ).text.strip()

                    rating = parent_element.find_element(
                        By.CSS_SELECTOR, "div.c82435a4b8 div.c066246e13 div.c1edfbabcb div.aca0ade214 div.aaee4e7cd3 div.aca0ade214 div.d6767e681c div.d8c86a593f span div.b3f3c831be"
                    ).get_attribute("aria-label")

                    review_no = parent_element.find_element(
                        By.CSS_SELECTOR, "div.c82435a4b8 div.c066246e13 div.c1edfbabcb div.aca0ade214 div div.aca0ade214.ebac6e22e9 div.aca0ade214.a5f1aae5b2 a span div.aca0ade214.aaf30230d9 div.aaee4e7cd3.e7a57abb1e.a29749fd9f div.abf093bdfe"
                    ).text.strip()

                    source = parent_element.find_element(
                        By.CSS_SELECTOR, "div.c82435a4b8 div.c066246e13 div.a5922b8ca1 div.e952b01718 a"
                    ).get_attribute("href")

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
            if i == 40:
                break

            next_button = self.driver.find_element(By.XPATH, "//button[@aria-label='Next page']")
            next_button.click()
            time.sleep(5)
