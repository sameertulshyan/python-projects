#!/usr/bin/python3

import cgi
import sqlite3

import cgitb
cgitb.enable()

print("Content-Type: text/html\r\n\r\n")
print('''<!DOCTYPE html>
	 <head>
         <title>Tobacco Usage 1995-2010</title>
         <link href="style.css" type="text/css"   rel="stylesheet" />
	 </head>
	 <body>
     <h1>Tobacco Usage 1995-2010</h1>''')

user_form = cgi.FieldStorage()
display_all = user_form["display"].value
query = ""

if display_all == "Yes":
    print("<p>You asked for all records from the dataset:</p>")
    query = "SELECT * FROM tobacco ORDER BY " + user_form["sort"].value
else:
    state = user_form["state"].value
    sort = user_form["sort"].value
    if sort == "data_year DESC":
        sort_english = " most recent year first."
    else:
        sort_english = " most recent year last."
    print("<p>You asked for data from " + state + " ordered by" + sort_english + "</p>")
    query = '''SELECT * FROM tobacco WHERE data_state="''' + state + '''" ORDER BY ''' + sort
    
connection = sqlite3.connect('tobacco.db')
c = connection.cursor()
c.execute(query)

print("<table>")
print("<tr>")
print("<th>Year</th>")
print("<th>State</th>")
print("<th>Smoke everyday</th>")
print("<th>Smoke some days</th>")
print("<th>Former smoker</th>")
print("<th>Never smoked</th>")
print("</tr>")

for year,state,everyday,some,former,never in c:
    print ("<tr>")
    print ("\t<td>"+str(year)        +"</td>")
    print ("\t<td>"+state       +"</td>")
    print ("\t<td>"+str(everyday)      +"</td>")
    print ("\t<td>"+str(some) +"</td>")
    print ("\t<td>"+str(former) +"</td>")
    print ("\t<td>"+str(never) +"</td>")
    print ("</tr>")

print("</table>")

c.close()

print("</body>")
print("</html>")
