import configparser
import logging
from utils import fetch_ip, setup_logging, clean_old_logs
from datetime import datetime
import smtplib
from email.mime.text import MIMEText

# Load config
config = configparser.ConfigParser()
config.read("config.ini")

api_url = config["DEFAULT"]["api_url"]
log_dir = config["DEFAULT"]["log_dir"]
cleanup_days = int(config["DEFAULT"]["cleanup_days"])

# Setup logging
log_file = setup_logging(log_dir)
logging.info("Task Bot Started")

# Fetch public IP
try:
    ip = fetch_ip(api_url)
    logging.info(f"Fetched IP: {ip}")
except Exception as e:
    logging.error(f"Error fetching IP: {e}")
    ip = "Failed to retrieve"

# Clean logs
deleted = clean_old_logs(log_dir, cleanup_days)
for file in deleted:
    logging.info(f"Deleted old log: {file}")

# Email summary (optional)
def send_email(subject, body):
    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = config["email"]["sender"]
    msg["To"] = config["email"]["receiver"]

    with smtplib.SMTP(config["email"]["smtp_server"], int(config["email"]["smtp_port"])) as server:
        server.starttls()
        server.login(config["email"]["sender"], config["email"]["password"])
        server.send_message(msg)

summary = f"Task Bot Report - {datetime.now()}\nIP: {ip}\nDeleted Logs: {deleted}"
logging.info("Email Summary Sent")
# send_email("Task Bot Report", summary)  # Uncomment to enable email
