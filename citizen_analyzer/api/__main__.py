from aiohttp import web

from citizen_analyzer.app import app

if __name__ == '__main__':
    web.run_app(app)
