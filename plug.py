import requests
from datetime import datetime, timedelta
from astral.sun import sun
from astral import LocationInfo
import pytz
import time

# Using webhook key
IFTTT_WEBHOOK_KEY = 'Your_Webhook_Key'
IFTTT_EVENT_NAME_ON = 'Plug_OnOff'

# location information
location = LocationInfo("County", "Country", latitude= "Your Latitude",longitude= "Your longitude")

# Calculate sunset time for today
sunset_time_utc = sun(location.observer, date=datetime.now()).get("sunset")
sunset_time_local = sunset_time_utc.astimezone(pytz.timezone(location.timezone))

# Calculate time difference to wait until sunset
current_time = datetime.now(pytz.timezone(location.timezone))
time_difference = sunset_time_local - current_time
time_to_wait_seconds = max(0, time_difference.total_seconds())

print(f"Waiting until sunset at {sunset_time_local.strftime('%Y-%m-%d %H:%M:%S')}")
# Wait until sunset
time.sleep(time_to_wait_seconds)

# Trigger IFTTT event to turn on the smart plug
url_on = f'https://maker.ifttt.com/trigger/{IFTTT_EVENT_NAME_ON}/with/key/{IFTTT_WEBHOOK_KEY}'
requests.post(url_on)

print("Smart plug turned ON at sunset!")
