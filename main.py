from websites import evs
import os
from dotenv import load_dotenv
load_dotenv()

EVS = evs.EVScraper(
    "https://www.caranddriver.com/news/g29994375/future-electric-cars-trucks/",
    "upcoming-evs.json"
)
EVS.run()