from setup import WebScraper
from selenium.webdriver.common.by import By


class ExpediaScraper(WebScraper):
    def perform_scraping(self):
        # Add your custom scraping logic here
        # This will override the perform_scraping method from the base class
        parent_elements = self.driver.find_elements(
            By.CSS_SELECTOR, "div[data-stid='section-results'] div[data-stid='property-listing-results'] div.uitk-spacing div.uitk-card div.uitk-layout-grid div.uitk-card-content-section")

        # Loop through each parent element
        for parent_element in parent_elements:
            # finding data from site
            title = parent_element.find_element(
                By.CSS_SELECTOR, "div.uitk-layout-flex div.uitk-spacing div.uitk-layout-flex h3"
            ).text.strip()

            # creating json record
            result_data = {
                "Title": title,
                "Location": "",
                "Address": "",
                "PostCode": "",
                "Review": 0,
                "ReviewNumber": 0,
                "Stars": "",
                "PropertyType": "",
                "Source": ""
            }
            self.entries.append(result_data)

    
