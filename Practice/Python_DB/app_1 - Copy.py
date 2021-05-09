import mysql.connector as view
import cgi


def printHeader(title):
    print("""Content-type: text/html
        <?xml version="1.0" PUBLIC
        "-//W3C//DTD XHTML 1.0 Transitional//EN"
        "DTD/xhtml1-transitional.dtd">
        <html xmlns = "http://www.w3.org/1999/xhtml"
        xml:lang="en"lang="en">
        <head><title>%s</title><head>
        <body>"""%title)



#Syntax to connect to a database...
connection = view.connect(host = 'localhost',
                          database='Books',
                          user='root',
                          password='Sul03314307703')

#Check whether the database is connected or not...
if connection.is_connected():
    print("Connected to MySQL database")

cursor = connection.cursor()
res1 = cursor.execute("SELECT * FROM books.author")

#******   Description of the Each field in the database*************
#print(cursor.description)
allFields = cursor.description
for i in cursor.description:
    print(i[0])
#--------------------------------------------------------------------------
records = cursor.fetchall()

#***************Print Records****************
for i in records:
    print(i)
#------------------------------------------------------------



#Obtain user query specifications...
form = cgi.FieldStorage()

if "sortBy" in form:
    sortBy = form["sortBy"].value
else:
    sortBy = allFields[0][0]


if "sortOrder" in form:
    sortOrder = form["sortOrder"].value
else:
    sortOrder = "ASC"

#   Query all records from Authors Table
cursor.execute("SELECT * FROM books.author ORDER BY %s %s", (sortBy, sortOrder))
allRecords = cursor.fetchall()
cursor.close()
connection.close()

#output results in table
printHeader("Author table from Books")
print("""\n<table border =  "1" cellpadding = "3" >
<tr bgcolor = "silver" > """)


# create table header
for field in allFields:
    print("<td>%s</td>"%field[0])

print("</tr>")


for author in allRecords:
    print("<tr>")

    for item in author:
        print("<td>%s</td>"%item)
    print("</tr>")
print("</table>")


#   obtain sorting method from user
print("""\n<form method = "POST" action = "app_1.py">
Sort Br:<br />""")

for field in allFields:
    print("""<input type="radio" name="sortBy" value="%s" />"""%field[0])
    print("<br />")

print("""<br />\nSort Order:<br />
<input type="radio" name="sortOrder" value="ASC" checked="checked" />
Ascending""")
print("""<input type="radio" name="sortOrder" value="DESC" />Descending""")

print("""<br /><br />\n<input type="submit" value="Sort" />
</form>\n\n</body>\n</html>""")
