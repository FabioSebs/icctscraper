from websites import otto
import os
from dotenv import load_dotenv
load_dotenv()

EVS = otto.OttoScraper(
    "https://www.oto.com/en/mobil-terbaru/elektrik",
    "latest-evs.json"
)
EVS.run()