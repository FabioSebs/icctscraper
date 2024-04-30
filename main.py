from websites import ziggs
import os
from dotenv import load_dotenv
load_dotenv()

EVS = ziggs.ZiggsScraper(
    "https://www.zigwheels.co.id/motor-baru/elektrik/",
    "latest-motorcycles.json"
)
EVS.run()