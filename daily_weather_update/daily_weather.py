'''
The Daily Weather app obtains the most recent weather data from weather.gov and emails it to the specified recipients at 9am every day.
The default station is set to Central Park, NYC.

Please ensure that you have entered your email address and password in the send_html_file module.

Note: usage requires installation of the schedule package ($ pip install schedule)

Created on 10 Jan 2018

@author: Sameer Tulshyan
'''

from Get_Weather_Data import get_weather_data
from Create_Html_file import create_html_report 
from Send_Html_file import send_gmail

from collections import OrderedDict
from time import sleep
from pprint import pprint
import schedule

def job():
    """Function that will be called based on the scheduled frequency"""
    pprint(schedule.jobs)
    weather_dict, icon = get_weather_data('KNYC') #default station is KNYC, can be changed to any valid station code
    weather_dict_ordered = OrderedDict(sorted(weather_dict.items())) #dictionary must be ordered to align with our HTML template
    
    email_file = "Email_File.html"
    create_html_report(weather_dict_ordered, icon, email_file)
    send_gmail(email_file)


schedule.every.day.at("9:00").do(job) #note that the time is in 24 hours format, so this refers to 9:00 am

#infinite loop required for usage of the schedule package
while True:
    schedule.run_pending()
    sleep(1)
    
    
    