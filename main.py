from websites import expedia
import os
from dotenv import load_dotenv
load_dotenv()

ExpediaScraper = expedia.ExpediaScraper(os.getenv("EXPEDIA"), "expedia.json")
ExpediaScraper.run()