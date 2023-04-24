from aiohttp import web
from controllers import import_citizens


def setup_routes(app: web.Application):
    app.router.add_post('/imports', import_citizens)
    # app.router.add_patch('imports/{import_id}/citizens/{citizen_id}')
