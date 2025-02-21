from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from dotenv import load_dotenv
import os
import re

# Slack channel to send the message to
SLACK_API_TOKEN = "xoxb-6253138637332-6243077942519-9yBMEnwdIgBRMOmQ3anhRQOA"

def sendSlackWebhook(file_path):
    client = WebClient(token=SLACK_API_TOKEN)
    try:
        response = client.files_upload(
            channels="#python-test",
            file=file_path,
            title=f"위험정보 포함 파일입니다."
        )
        print(f"정상적으로 보냄")
    except SlackApiError as e:
        print(f"오류 발생 {e}")
        
def smtpMail():
    load_dotenv()
    SECRET_ID = os.getenv('ID')
    SECRET_PASS = os.getenv('PASS')

    smtp= smtplib.SMTP('smtp.naver.com',587)
    smtp.ehlo()
    smtp.starttls()

    smtp.login(SECRET_ID,SECRET_PASS)

    myemail = 'ggggame93@naver.com'
    youremail = 'ggggame93@naver.com'

    msg = MIMEMultipart()

    msg['Subject'] ="위험정보 포함 파일 입니다."
    msg['From'] = myemail
    msg['To'] = youremail

    text ="""
            <html>
            <body>
            <h2>위험 파일 입니다.</h2>
            </body>
            </html>
        """
        
    contentPart = MIMEText(text,'html')
    msg.attach(contentPart)

    file_name='access.log'
    etc_file_path = fr'{file_name}'
    with open (etc_file_path,'rb') as f:
        etc_part = MIMEApplication(f.read())
        etc_part.add_header('Content-Disposition','attachment', filename=etc_file_path)
        msg.attach(etc_part)
            
    smtp.sendmail(myemail,youremail,msg.as_string())
    smtp.quit()

#for file_name in files:
output_path = f"{file_name}"
sendSlackWebhook(output_path)
