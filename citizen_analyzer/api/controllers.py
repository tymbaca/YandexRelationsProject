from aiohttp import web


# region test

async def load_and_return_json(request: web.Request):
    response = await request.text()
    return web.Response(status=201, text=response)


async def import_citizens(request: web.Request) -> web.Response:
    check_json(request)
    pass

# endregion


