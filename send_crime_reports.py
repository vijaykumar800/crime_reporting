from utils import email_operations,google_operations,report_operations
from settings import logger

logger.info('calling read_report_csv function from main module')
read_dataframe = report_operations.read_report_csv('D:\\projects\\big_query\\email.csv')

logger.info('calling processing_report_file function from main module')
report_operations.process_report_request(read_dataframe)


logger.info('done')







