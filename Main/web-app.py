from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response

def hello_world(request):
    return Response('hello world !')

if __name__ == '__main__':
    with Configurator() as config:
        config.add_route('hello', '/')
        n
        config.add_view(hello_world, route_name = 'hello')
        app = config.make_wsgi_app()
    sever = make_server('0.0.0.0', 6543, app)
    sever.serve_forever()
