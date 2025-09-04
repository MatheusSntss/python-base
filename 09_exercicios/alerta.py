#!/usr/bin/env python3
"""
Temperature alarm

Write a script that asks the user for the current temperature and humidity level.
Depending on the conditions, an alert message will be displayed:

temperature greater than 45: "ALERT!!! 🥵 Extreme heat danger"
temperature greater than 30 and temp times 3 is greater than or equal to humidity:
    "ALERT!!! 🥵♒ Humid heat danger"
temp between 10 and 30: “😀 Normal”
temp between 0 and 10: “🥶 Cold”
temp <0: “ALERT!!! ⛄ Extreme cold.”

ex:
python3 alert.py
temperature: 30
humidity: 90...

“ALERT!!! 🥵♒ Humid heat hazard”

"""
import sys
import logging
log = logging.Logger("alerta")

info = {"temperature":None, "humidity":None}

for key in info.keys():
    try:
       info[key] = float(input(f"What is current {key}: ").strip())
    except ValueError:
        log.error(f"{key.capitalize()} invalid")
        sys.exit(1)
        
temperature = info["temperature"]
humidity = info["humidity"]        
if temperature > 45:
    print("ALERT!!! 🥵 Extreme heat hazard")
elif temperature > 30 and temperature * 3 >= humidity:
    print("ALERT!!! 🥵♒ Danger of humid heat")
elif temperature >= 10 and temperature <= 30:
    # elif 10 <= temp <= 30:
    # elif temp in range(1, 31):
    print("😀 regular")
elif temperature >= 0 and temperature <= 10:
    print("🥶 Cold")
elif temperature < 0:
    print("ALERT!!! ⛄ Extreme Cold.")
