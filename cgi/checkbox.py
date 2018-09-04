# cat cgi-bin/checkbox.py

#!/usr/bin/python

# Import modules for CGI handling
import cgi, cgitb

# Create instance of FieldStorage
form = cgi.FieldStorage()

# Get data from fields
if form.getvalue('Python'):
        course_flag = "ON"
else:
   course_flag = "OFF"

if form.getvalue('Perl'):
   Perl_flag = "ON"
else:
   Perl_flag = "OFF"

print ("Content-type:text/html\r\n\r\n")
print ("<html>")
print ("<head>")
print ("<title>Checkbox - Third CGI Program</title>")
print ("</head>")
print ("<body>")
print ("<h2> CheckBox Python is : %s</h2>" % course_flag)
print ("<h2> CheckBox Perl is : %s</h2>" % Perl_flag)
print ("</body>")
print ("</html>")

