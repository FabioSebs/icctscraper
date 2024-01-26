from websites import bookings
import os
from dotenv import load_dotenv
load_dotenv()

Bookings = bookings.BookingsScraper(
    "https://theicct.org/insight-analysis/publications/",
    "books.json"
)
Bookings.run()