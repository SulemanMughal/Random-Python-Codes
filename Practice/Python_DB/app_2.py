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

connection = 
