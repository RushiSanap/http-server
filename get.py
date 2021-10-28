#!/usr/bin/python
import os
import mimetypes  # to check file type (class/subclass)
import gzip
from headers import *

class Get:
    def response_line(self, status_code):
        # Returns response line (as bytes)
        reason = status_codes[status_code]
        response_line = 'HTTP/1.1 %s %s\r\n' % (status_code, reason)
        return response_line.encode()

    def HTTP_501_handler(self, request, data):
        # Returns 501 HTTP response if the requested method hasn't been implemented.
        response_line = self.response_line(status_code=501)

        gen, req = request.parse(data)
        ent = EntityHeader()
        response_headers = gen.general_header() + ent.entity_header() + req.request_header()
        blank_line = b'\r\n'
        response_body = b'<h1>501 Not Implemented</h1>'
        return b"".join([response_line, response_headers, blank_line, response_body])


    def GET(self, request, data):
        gen, req = request.parse(data)

        # keep the general headers as it is i.e 'gen'
        # use the request headers
        acpt = getattr(req, 'Accept')
        acpt_charset = getattr(req, 'Accept_Charset')
        acpt_enco = getattr(req, 'Accept_Encoding')

        path = request.URI
        if path == '/':
            # If path is empty, that means user is at the homepage so just serve index.html
            path = '/index.html'

        if os.path.exists(path) and not os.path.isdir(path):  # don't serve directories
            
            response_line = self.response_line(200)
            with open(path, 'rb') as f:
                response_body = f.read()

            # this is something like nieve solution
            # go into deep
            if acpt_enco.find('gzip'):
                response_body = gzip.compress(response_body)
            elif acpt_enco == 'compress':
                pass
            elif acpt_enco == 'deflate':
                pass
            elif acpt_enco == 'br':
                pass
            elif acpt_enco == 'identity':
                pass
            elif acpt_enco == '*':
                pass
            else:
                pass
            
            # find out a file's MIME type if nothing is found, just send `text/html`
            content_type = mimetypes.guess_type(path)[0] or 'text/html'

            ent = EntityHeader('gzip', content_type, str(len(response_body)))

            response_headers = gen.general_header() + req.request_header()
        else:
            ent = EntityHeader()

            response_line = self.response_line(404)
            response_headers = gen.general_header() + ent.entity_header() + req.request_header()
            response_body = b'<h1>404 Not Found</h1>'

        blank_line = b'\r\n\r\n'
        response = b"".join([response_line, response_headers.encode(), blank_line, response_body])
        return response



