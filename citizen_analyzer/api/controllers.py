import json
from aiohttp import web
from aiohttp.web import Response, Request
from pydantic import ValidationError
from pydantic.main import Model

import citizen_analyzer.api as api
import citizen_analyzer.db as db

from api.services import handle_import_and_return_id
from api.pydantic_models import ImportModel, CitizenModel

# from citizen_analyzer.api.pydantic_models import Import, Citizen


# region test

async def import_citizens(request: Request) -> web.Response:
    body: str = await request.text()
    try:
        body_model: ImportModel = ImportModel.parse_raw(body)
    except ValidationError:
        return Response(status=400)

    try:
        import_id = handle_import_and_return_id(body_model)
        return_data = {
            "data": {
                "import_id": import_id
            }
        }
        return Response(json=return_data, status=201)
    except ...:
        ...

# endregion
