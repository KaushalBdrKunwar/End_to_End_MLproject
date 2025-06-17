import logging

# to track all the excecution
import os
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

logs_path = os.path.join(os.getcwd(),"logs",LOG_FILE) # creates complete path for log cwd/logs->new folder/log_file.

os.makedirs(logs_path,exist_ok=True)

LOG_FILE_PATH = os.path.join(logs_path,LOG_FILE)

# Create a log.
logging.basicConfig(
  filename=LOG_FILE_PATH,
  format='%(asctime)s - %(levelname)s - %(message)s',
  level=logging.INFO,
)
