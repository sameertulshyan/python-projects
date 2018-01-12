'''
Module containing a function to obtain weather data from weather.gov in an xml format and parse the data into a dictionary based on each data tag

Created on 10 Jan 2018

@author: Sameer Tulshyan
'''

#Dictionary containing keys that represent the XML Tags we are looking for
weather_data_tags_dict = {
    'observation_time': '',
    'weather': '',
    'temp_f':  '',
    'temp_c':  '',
    'dewpoint_f': '',
    'dewpoint_c': '',
    'relative_humidity': '',
    'wind_string':   '',
    'visibility_mi': '',
    'pressure_string': '',
    'pressure_in': '',
    'location': ''
    }

import urllib.request
from pprint import pprint

def get_weather_data(station_code='KNYC'):
    """Function to query the website for data based on the user-submitted station code, update the dictionary values and get the image url"""
    url_general = 'http://www.weather.gov/xml/current_obs/{}.xml'
    url = url_general.format(station_code)
    request = urllib.request.urlopen(url)
    content = request.read().decode()

    # Using ElementTree to retrieve specific tags from the xml
    import xml.etree.ElementTree as ET
    xml_root = ET.fromstring(content)
    
    # Update the dictionary values with data from the xml
    for data_point in weather_data_tags_dict.keys():
            try:
                weather_data_tags_dict[data_point] = xml_root.find(data_point).text
            except: #handle the case where certain data points are not available for a station
                weather_data_tags_dict[data_point] = "-"

    # Get the url for the image representing the weather icon
    icon_url_base = xml_root.find('icon_url_base' ).text
    icon_url_name = xml_root.find('icon_url_name' ).text
    icon_url = icon_url_base + icon_url_name
    
    return weather_data_tags_dict, icon_url


# testing section, actual implementation will occur in another module
if __name__ == '__main__':
    weather_dict, icon = get_weather_data()
    pprint(weather_dict)
    print(icon)