from setup import WebScraper
from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()
api_key = os.getenv("EXPEDIA")
print(api_key)

class ExpediaScraper(WebScraper):
    def perform_scraping(self):
        # Add your custom scraping logic here
        # This will override the perform_scraping method from the base class
        print(api_key)

