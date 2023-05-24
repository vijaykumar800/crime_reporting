import pandas as pd
from settings import logger
from settings import config_json
from datetime import datetime
from utils import google_operations,email_operations


logger.info('initializing datetime function')
today_time = datetime.now()
logger.info(today_time)
logger.info('formatting datetime')
today_time = today_time.strftime("%d-%M-%Y-%H-%M-%S-%p")
logger.info(today_time)


def remove_space(string):
    pattern = re.compile(r'\s+')
    return re.sub(pattern,'',string)

def read_report_csv(csv_input):
    logger.info('entering read_report_csv function')
    logger.debug('reading report csv file to pandas')
    crime_request_df = pd.read_csv(csv_input)
    logger.debug('returning csv file as dataframe')
    logger.debug('printing dataframe')
    logger.debug(crime_request_df)
    logger.info('read_report function end')
    return crime_request_df


def to_export_csv_file(dataframe,report_type,time_stamp):
    """f'{report_type} {time_stamp}'"""
    logger.debug('creating file name')
    # to_csv_filename=f'{report_type}_{time_stamp}.csv'
    # to_csv_filename = eval(config_json["app_config"]["output_filename"])
    to_csv_filename = config_json["app_config"]["output_filename"].format(report_type=report_type,time_stamp=time_stamp)
    logger.debug('converting dataframe to csv file to the specified location')
    dataframe.to_csv(to_csv_filename,index=False)
    logger.debug('returning csv file')
    logger.info('to_export_csv_file function end')
    return to_csv_filename


def process_report_request(report_dataframe):
    logger.info('entering process_report_request function')
    """
    using iter rows iterate each row from report dataframe
    for each row using report type and timestamp retrieve
    crime records from big query table and convert the output
    into dataframe .then convert the dataframe into csv file
    and email csv
    """
    logger.info('iterating dataframe to use the column values')
    logger.info('\n\n')
    for index,row in report_dataframe.iterrows():
        logger.debug(f"report_type:{row['report_type']}---time_period:{row['time_period']}")
        logger.debug(f'current_report_record_no:{index+1}---total_report_record_count:{len(report_dataframe)}')
        logger.info('\n')
        report_type = report_type.capitalize()
        logger.info(report_type)
        report_type = remove_space(report_type)
        logger.info(report_type)
        report_df = google_operations.get_crime_data(row['report_type'],row['time_period'])
        logger.debug('calling to_export_csv_file function')
        if report_df.empty:
            logger.warning('no data returned from bigquery')
            continue
        to_csv_file=to_export_csv_file(report_df,row['report_type'],today_time)
        logger.debug('calling send_email function')
        email_operations.send_email(to_csv_file,row['email_address'],row['report_type'])
    logger.info('process_report_request function end')







































