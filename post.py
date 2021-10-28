class Post:
    def POST(self, request):
        path = request.URI
        if path == '\\':
            path = 'index.html'