from wsgiref.simple_server import make_server
from cgi import parse_qs
import json

def application(environ, start_response):
   
    try:
        request_body_size = int(environ.get('CONTENT_LENGTH', 0))
    except ValueError:
        request_body_size = 0

    request_body = environ['wsgi.input'].read(request_body_size)
    d = parse_qs(request_body)

    sentence = d.get('sentence',[''])[0]
    character = d.get('character', [''])[0]
  
    length_sentence = len(sentence)
    character_count = sentence.count(character)

    status = '200 OK'	
    response_body = json.dumps({'length': length_sentence , 'count' : character_count)})
    

    response_headers = [
        ('Content-Type', 'application/json'),
        ('Content-Length', str(len(response_body)))
    ]

    start_response(status, response_headers)
    return[response_body]


httpd = make_server('192.168.43.117', 8051, application)

httpd.serve_forever()
