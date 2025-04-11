# config.py

import os

# AWS S3 Configuration
S3_BUCKET_NAME = "earthquake-etl-bucket"
S3_REGION = ""  # Change this to the appropriate AWS region



# API Configuration for Earthquake Data (USGS)
API_URL = "https://earthquake.usgs.gov/fdsnws/event/1/application.json"

# Data Processing Configuration
MAX_RESULTS = 500  # You can adjust this depending on how many results you want to fetch

# Other configurable parameters
LOG_LEVEL = "INFO"  # Choose log level (DEBUG, INFO, WARNING, ERROR, CRITICAL)