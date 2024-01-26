from setup import WebScraper
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time


class ExpediaScraper(WebScraper):
    def perform_scraping(self):
        time.sleep(10)
        # load more button
        load_more_button = self.driver.find_element(By.XPATH, "//button[contains(text(), 'Show More')]")
        load_more_button.click()

        time.sleep(10)
        

        # parent
        parent_elements = self.driver.find_elements(
            By.CSS_SELECTOR, "div[data-stid='section-results'] div[data-stid='property-listing-results'] div.uitk-spacing div.uitk-card"
        )

        Source = self

        # Loop through each parent element
        for parent_element in parent_elements:
            try:
                # finding data from site
                title = parent_element.find_element(
                    By.CSS_SELECTOR, "div.uitk-layout-grid div.uitk-card-content-section div.uitk-layout-flex div.uitk-spacing div.uitk-layout-flex div.uitk-layout-grid h3"
                ).text.strip()

                location = parent_element.find_element(
                    By.CSS_SELECTOR, "div.uitk-layout-grid div.uitk-card-content-section div.uitk-layout-flex div.uitk-spacing div.uitk-text"
                ).text.strip()

                Review_elements = parent_element.find_elements(
                    By.CSS_SELECTOR, "div.uitk-layout-grid div.uitk-card-content-section div.uitk-layout-flex div.uitk-layout-grid div.uitk-layout-grid-item div.uitk-layout-flex div.uitk-layout-flex div.uitk-layout-flex span"
                )

                Review = Review_elements[0].text.strip() if Review_elements else '0'
                Review = Review.split('\n')[0]

                ReviewNumber = parent_element.find_elements(
                    By.CSS_SELECTOR, "div.uitk-layout-grid div.uitk-card-content-section div.uitk-layout-flex div.uitk-layout-grid div.uitk-layout-grid-item div.uitk-layout-flex div.uitk-layout-flex div.uitk-layout-flex div.uitk-layout-flex span span"
                )
                ReviewNumber = ReviewNumber[1].text.strip() if ReviewNumber else '0'

                Price = parent_element.find_element(
                    By.CSS_SELECTOR, "div.uitk-layout-grid div.uitk-card-content-section div.uitk-layout-flex div.uitk-layout-grid div.uitk-layout-flex div.uitk-layout-flex div div.uitk-layout-flex div.uitk-text.uitk-type-end.uitk-type-200.uitk-text-default-theme"
                ).text.strip()

                Source = parent_element.find_element(
                    By.CSS_SELECTOR, "a.uitk-card-link"
                )
                Source = Source.get_attribute("href")
                
                # creating json record
                result_data = {
                    "Title": title,
                    "Location": location,
                    "Address": "",
                    "PostCode": "",
                    "Review": Review,
                    "ReviewNumber": ReviewNumber,
                    "Price": Price,
                    "PropertyType": "",
                    "Source": Source
                }

                print(result_data)
                self.entries.append(result_data)
            
            except Exception as e:
                continue
            
            

    
