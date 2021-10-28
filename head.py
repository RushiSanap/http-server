import os, mimetypes
from headers import *
class Head:
    def HEAD(self, request, data):
        gen, req = request.parse(data)

        # keep the general headers as it is i.e 'gen'
        # use the request headers
        acpt = getattr(req, 'Accept')
        acpt_charset = getattr(req, 'Accept_Charset')
        acpt_enco = getattr(req, 'Accept_Encoding')


        path = request.URI
        if path == '\\':
            # If path is empty, that means user is at the homepage so just serve index.html
            path = 'index.html'

        if os.path.exists(path) and not os.path.isdir(path):  # don't serve directories
            
            response_line = self.response_line(200)
            
            # find out a file's MIME type if nothing is found, just send `text/html`
            content_type = mimetypes.guess_type(path)[0] or 'text/html'

            ent = EntityHeader('gzip', content_type)

            response_headers = gen.general_header() + ent.entity_header() + req.request_header()
        else:
            ent = EntityHeader()

            response_line = self.response_line(404)
            response_headers = gen.general_header() + ent.entity_header() + req.request_header()
            
        response = b"".join([response_line, response_headers.encode()])
        return response
