import os
import logging

logging_str = "[%(asctime)s: %(levelname)s: %(module)s] %(message)s"
log_dir = "logs1"
os.makedirs(log_dir,exist_ok=True)
logging.basicConfig(filename=os.path.join(log_dir,"running_log1.log"),level=logging.INFO, format=logging_str,filemode="a")

logging.info("Hello, World!")
logging.info("Sarvesh Kamble")