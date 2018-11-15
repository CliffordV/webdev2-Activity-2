#!C:/Users/VanderClifford/AppData/Local/Programs/Python/Python35-32/python.exe

import cgi
import cgitb
from datetime import date
cgitb.enable()

print("Content-type: text/html \n")
print()

form = cgi.FieldStorage()
month = form.getvalue('month')
day = form.getvalue('day')

date_today = date.today()

if int(date_today.month) >= int(month):
    birthday = date(int(date_today.year+1), int(month), int(day))
    str(birthday - date_today)
    left_days = (birthday - date_today).days
else:
    birthday = date(int(date_today.year), int(month), int(day))
    str(birthday - date_today)
    left_days = (birthday - date_today).days

	
print("""
	<!DOCTYPE html>
	<html>
		<head>
			<link rel="icon" type="image/png" href="icn.png">
			<title>Left Days</title>
			<link href='https://fonts.googleapis.com/css?family=Bangers' rel='stylesheet' type='text/css'>
			<style>
				body {
					text-align: center;
					font-family: helvetica;
					background-image: url("bckground.jpg");
					background-size: 1366px 690px;
					background-repeat: no-repeat;
					position: fixed;
				    overflow-y: scroll;
				    width: 100%;
				}
				h3{
					font-family: 'Bangers', Georgia, Serif;
					font-size: 4em;
					text-shadow: 3px 3px white;
					color: rgba(50, 50, 50, 1);
				}
				h1{
					font-family: 'Bangers', Georgia, Serif;
					font-size: 4em;
					text-shadow: 3px 3px white;
					color: rgba(50, 50, 50, 1);
				img {
					width: 40%;
					height: 40%;
					margin: 0 0 0 15px;
				}
			</style>
		</head>

		<body>
		<br/><br/><br/><br/>
		""")

print("<h3>There are only</h3>")
print("<h1>%d Days</h2>"% left_days)
print("<h3>until your BIRTHDAY</h3>")

		
print("<a href=\"enterBirthdate.html\"></a>")

print("""
		</body>
	</html>
	""")