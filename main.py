from websites import ziggs
import os
from dotenv import load_dotenv
load_dotenv()

EVS = ziggs.ZiggsScraper(
    "https://www.zigwheels.co.id/en/mobil-baru/elektrik/",
    "latest-evs2.json"
)
EVS.run()