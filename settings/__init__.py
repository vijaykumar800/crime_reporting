import sys
import json
from loguru import logger

with open('settings/config.json','r') as f:
    config_json = json.load(f)

logger.add(sys.stdout, backtrace=False, level="DEBUG")
logger.add('run_info.log',
           rotation=config_json["loguru"]["rotation"],
           retention=config_json["loguru"]["retention"],
           level="INFO")

logger.add('run_warning.log',
           rotation=config_json["loguru"]["rotation"],
           retention=config_json["loguru"]["retention"],
           level="WARNING")

logger.add(config_json["loguru"]["logfile"],
           rotation=config_json["loguru"]["rotation"],
           retention=config_json["loguru"]["retention"],
           level=config_json["loguru"]["level"],
           backtrace=False)






