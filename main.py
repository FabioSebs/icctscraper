from websites import lacb
import os
from dotenv import load_dotenv
load_dotenv()

LACB = lacb.LACBScraper(
    "https://www.allrecipes.com/recipes/237/world-cuisine/latin-american/",
    "lacb.json"
)
LACB.run()