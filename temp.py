from sense_hat import SenseHat
import time
import requests
from dotenv import dotenv_values

# Initialize Sense HAT
sense = SenseHat()

# Threshold for temperature (in Celsius)
threshold_temperature = 29.0

# IFTTT Webhooks URL and Event Name
ifttt_url = "https://maker.ifttt.com/trigger/Temp_Alert/with/key/Your_webhooks_key"

#load auth token values from .env file
config = dotenv_values(".env")

# Read temperature from Sense HAT
def get_temperature():
    temperature = sense.get_temperature()
    return temperature

# Send an HTTP request to trigger IFTTT event
def trigger_ifttt_event():
    requests.post(ifttt_url)
# Main loop to continuously monitor temperature
try:
    while True:
         current_temperature=round(sense.get_temperature(),2)
         print(f"Temperature: {current_temperature}°C")

        # Check if the temperature falls below the threshold
         if current_temperature < threshold_temperature:
            print("Temperature below threshold!")

            # Trigger IFTTT event to boost heating
            trigger_ifttt_event()
            break
        # Pause for a 10 seconds
         time.sleep(10)

except KeyboardInterrupt:
        print("Terminated by User.")
