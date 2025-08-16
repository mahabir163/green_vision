import logging
import os
from from_root import from_root #it return to root directory
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime("%m_%d_%Y_%H_%M_%S")}.log"  
logs_path = os.path.join(from_root(),"logs",LOG_FILE)  #Current_root/logs(folder)/08_16_2025_12_01_25.log

os.makedirs(logs_path,exist_ok=True) #It make a directory or folder
LOG_FILE_PATH = os.path.join(logs_path,LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(name)s - %(levelname)s - %(message)s",  #Place holder of format, 's' refer to string format
    level=logging.DEBUG,
)
