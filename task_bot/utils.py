import os
import requests
import logging
from datetime import datetime, timedelta

def fetch_ip(api_url):
    response = requests.get(api_url)
    return response.json()["ip"]

def setup_logging(log_dir):
    os.makedirs(log_dir, exist_ok=True)
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    log_path = os.path.join(log_dir, f"log_{timestamp}.txt")
    logging.basicConfig(filename=log_path, level=logging.INFO)
    return log_path

def clean_old_logs(log_dir, days=3):
    now = datetime.now()
    deleted_files = []
    for file in os.listdir(log_dir):
        file_path = os.path.join(log_dir, file)
        if os.path.isfile(file_path):
            file_age = now - datetime.fromtimestamp(os.path.getmtime(file_path))
            if file_age.days >= days:
                os.remove(file_path)
                deleted_files.append(file)
    return deleted_files
