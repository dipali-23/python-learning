# import requests

# response = requests.get('https://api.github.com')
# print(response.status_code)
# print(response.json())
# print(response.headers)


# from datetime import datetime, timedelta

# now = datetime.now()
# print("Current time:", now)

# yesterday = now - timedelta(days=1)
# print("Yesterday:", yesterday.strftime("%Y-%m-%d %H:%M"))




# import os

# print(os.getcwd())                     # Current working directory
# os.makedirs("reports", exist_ok=True) 




# import subprocess

# subprocess.run(["open", "https://www.google.com"])  # Opens Google in the default web browser


# task1

import requests
import datetime
import os

# Get public IP
response = requests.get('https://api.ipify.org?format=json')
print(response.status_code)
print(response.json())

# Format timestamp for filename
timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

# Ensure logs directory exists
os.makedirs("logs", exist_ok=True)

# Create filename and write to file
filename = f"logs/log_{timestamp}.txt"
with open(filename, 'w') as file:
    file.write(f"Log entry at {timestamp}\n")
    file.write(f"public_ip: {response.json()['ip']}\n")
