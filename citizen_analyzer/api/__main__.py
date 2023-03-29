from aiohttp import web
from urls import setup_routes

app = web.Application()
setup_routes(app)

if __name__ == '__main__':
    web.run_app(app)
