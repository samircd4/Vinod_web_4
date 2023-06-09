from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
from mail_config import email_sender, email_pass


def send_mail(df):
    print('Sending email...')
    # Account info:
    email_rec = 'samircd4@gmail.com'
    # Email Info 
    message = MIMEMultipart()
    message['Subject'] = "New Data found from ecomm.sirim.my"
    
    html = MIMEText(df.to_html(index=False), 'html')
    message.attach(html)
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.starttls
        smtp.login(email_sender, email_pass)
        smtp.sendmail(email_sender, email_rec, message.as_string())
    print('Email sent!')