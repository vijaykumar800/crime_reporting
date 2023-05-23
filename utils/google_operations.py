
import json
from settings import config_json
from settings import logger
import re


from google.cloud import bigquery
from google.oauth2 import service_account
credentials = service_account.Credentials.from_service_account_file(config_json["gbq_config"]["credentials"])

project_id = config_json["gbq_config"]["project"]
client = bigquery.Client(credentials=credentials,project=project_id)


def remove(string):
    pattern = re.compile(r'\s+')
    return re.sub(pattern,'',string)


def get_crime_data(report_type,time_period):
    logger.info('entering get_crime_data function')
    logger.debug('printing sql query')
    report_type = report_type.capitalize()
    logger.info(report_type)
    report_type = remove(report_type)
    logger.info(report_type)
    report_sql=f"""SELECT *            
    FROM bigquery-public-data.austin_crime.crime 
    WHERE primary_type = '{report_type}' AND  
    date(timestamp) >= DATE_SUB(CURRENT_DATE(), INTERVAL {time_period} year);"""
    logger.debug(report_sql)
    logger.debug('start connect query to bigquery')
    query_job = client.query(report_sql)
    logger.debug('finish connecting query to bigquery')
    report_dataframe_records = query_job.result().to_dataframe()
    logger.debug('finish changing bigquery output table to dataframe and return dataframe')
    logger.info('get_crime_data function end')
    return report_dataframe_records



