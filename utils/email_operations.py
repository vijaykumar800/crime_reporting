from settings import config_json
import smtplib
from settings import logger
from email.message import EmailMessage


def send_email(attachment_report_file,email_address,report_type):
    if attachment_report_file != 'file is empty':
        logger.info('entering send email function')
        logger.debug('connecting to server')
        server=smtplib.SMTP(config_json["mail_config"]["host"],config_json["mail_config"]["port"])
        logger.debug('starting tls')
        server.starttls()
        logger.debug('logging in email using username password')
        server.login(config_json["mail_config"]["user_name"],config_json["mail_config"]["password"])
        from_address='vijaykumarrdhanapal@gmail.com'
        subject = f'{report_type} crime report'
        logger.debug('sending text content email')
        message=EmailMessage()
        message['Subject']=subject
        message['From']=from_address
        message['To']=email_address
        message.set_content('hello')
        logger.debug('opening attachment file')
        with open(attachment_report_file,'rb') as content_file:
            logger.debug('reading attachment file')
            content=content_file.read()
            logger.debug('setting attachment file type')
            message.add_attachment(content, maintype='text', subtype='csv', filename=attachment_report_file)
            logger.debug('sending attachment file in email')
        server.send_message(message)
        logger.info('send email function end')
        logger.info('\n\n\n')
    else:
        logger.debug('file is empty')

