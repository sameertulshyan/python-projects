'''
Created on 10 Jan 2018

@author: Sameer Tulshyan
'''


import smtplib
from email.mime.text import MIMEText
from datetime import datetime              

def send_gmail(msg_file):
    with open(msg_file, mode='rb') as message:              # Open report html file for reading
        msg = MIMEText(message.read(), 'html', 'html')      # Create html message
    
    msg['Subject'] = 'Daily Weather {}'.format(datetime.now().strftime("%Y-%m-%d"))
    msg['From'] = '<enter your email address here>'
    msg['To'] = '<recipient 1 email address>, <recipient 2 email address>'    
    
    server = smtplib.SMTP('smtp.gmail.com', port=587)
    server.ehlo()       
    server.starttls()   #place the SMTP connection in TLS (Transport Layer Security) mode.  
    server.ehlo() 
    server.login('<enter your email address here>', '<enter your email password here>')
    server.send_message(msg)
    server.close()

#---------------------------------------------------------------
if __name__ == '__main__':
    from Get_Weather_Data import get_weather_data
    from Create_Html_file import create_html_report 
    weather_dict, icon = get_weather_data()    
    email_file = "Email_File.html"
    create_html_report(weather_dict, icon, email_file)
    send_gmail(email_file)
    
    
    
    