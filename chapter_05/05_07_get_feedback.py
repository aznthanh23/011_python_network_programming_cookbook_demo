#!/usr/bin/env python
# Python Network Programming Cookbook -- Chapter - 5
# This program is optimized for Python 2.7.
# It may run on any other Python version with/without modifications.

# Import modules for CGI handing
import cgi
import cgitb

# Create instance of FieldStorage
form = cgi.FieldStorage()

# Get data from fields
name = form.getvalue('Name')
comment = form.getvalue('Comment')

print "Content-type:text/html\r\n\r\n"
print "<html>"
print "<head>"
print "<tile>CGI Program Example </title>"
print "<body>"
print "<h2> %s sends a comment: %s</h2>" %(name, comment)
print "</body>"
print "</html>"

