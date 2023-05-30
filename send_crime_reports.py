from utils import report_operations
from settings import logger
from settings import config_json


logger.info('calling read_report_csv function from main module')
read_dataframe = report_operations.read_report_csv(config_json['app_config']['input_filename'])

logger.info('calling processing_report_file function from main module')
report_operations.process_report_request(read_dataframe)


logger.info('done')







