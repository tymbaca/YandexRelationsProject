from aiohttp import web
from controllers import load_and_return_json, import_citizens


def setup_routes(app: web.Application):
    app.router.add_get('/', load_and_return_json)
    app.router.add_post('/imports', import_citizens)
    app.router.add_patch('imports/{import_id}/citizens/{citizen_id}')
