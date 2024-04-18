from websites import tripadvisor
import os
from dotenv import load_dotenv
load_dotenv()

Bookings = tripadvisor.TripAdvisorScraper(
    "https://www.tripadvisor.com/Search?searchSessionId=001291094b07f937.ssid&searchNearby=false&ssrc=h&q=bali&sid=B3D1899E7AD44DFA8EB486C24C019F291705646765454&blockRedirect=true&geo=1&rf=6",
    "triphotels.json"
)
Bookings.run()