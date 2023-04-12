import json
from loguru import logger

with open('settings/config.json','r') as f:
    config_json = json.load(f)
print(config_json)
logger.info(config_json["loguru"]["APP_NAME"])
logger.add(config_json["loguru"]["LOGFILE"],
           rotation=config_json["loguru"]["ROTATION"],
           retention=config_json["loguru"]["RETENTION"],
           level=config_json["loguru"]["LEVEL"])