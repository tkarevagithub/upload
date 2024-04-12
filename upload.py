# Python script for "HTML in easy steps" by Mike McGrath at www.ineasysteps.com
# Uploads selected file and displays confirmation of success or failure.
# It should be placed on the web server, in the directory configured for CGI scripts.
# THIS SCRIPT IS FOR DEMONSTRATION PURPOSES ONLY.

import cgi, os
import cgitb; cgitb.enable()
form = cgi.FieldStorage()

fileitem = form['Upload']
fn=''

if fileitem.filename:
  fn = os.path.basename(fileitem.filename)
  open( fn, 'wb').write( fileitem.file.read() )
  msg = 'Upload Success'
else:
  msg = 'Upload Failure'

print('''Content-Type:text/html; charset=utf-8
\r\n\r\n<!DOCTYPE HTML>
<html><title>Web Server Response</title>
<style>tr,th,td{border:2px solid Gray}</style>
<table style="width:500px"><tr><th>File<th>Status
<tr><td> %s <td> %s </tr></table>
<img src="pwrabyss.gif"> </html>''' % ( fn, msg ) )