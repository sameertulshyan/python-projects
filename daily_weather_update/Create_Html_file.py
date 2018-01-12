'''
Module to use the get_weather_data function and create a html report based on the data

Created on 10 Jan 2018

@author: Sameer Tulshyan
'''

from datetime import datetime

def create_html_report(data_dict, icon_url, html_file):
    """Function that builds a weather table and report in html"""
    alt_var = data_dict['weather'] #relevant text to display in case the image does not load
   
    #open the file in write mode    
    with open(html_file, mode='w') as html_output:
        html_output.write( '\t<tr><td align="center">' + datetime.now()
                       .strftime("%Y-%m-%d %H:%M:%S") +'</td></tr><br>\n' )
        html_output.write( '<img alt={} src={}>'.format(alt_var, icon_url)) #write the weather icon representing the weather
        html_output.write( '<br><span style="color:blue"><b>\tWeather Data:</b>\n' ) #write a title saying "Weather Data:"
        html_output.write( '<br>')    
        
        html_output.write( '<html><table border=1>\n' ) 
        
        #write the data into a table, using the dictionary where each key represents the type and the value represents the data point
        for key, value in data_dict.items():
            html_output.write( '<tr><td><b><span style="color:black">{:s}</b></td><td align="left"><span style="color:blue"><b>{:s}</b></td></tr>\n'.format(key, value))
        
        html_output.write( '</table></html>\n' )

#-----------------------------------------------------------
if __name__ == '__main__':
    from Get_Weather_Data import get_weather_data
    weather_dict, icon = get_weather_data()
    create_html_report(weather_dict, icon, "Email_File.html")
    
                
