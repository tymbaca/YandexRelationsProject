import pytest
import requests

from tests.generate_imports import ImportGenerator
from tests.api.values import incorrect_relatives
from citizen_analyzer.api import controllers

ENDPOINT = "http://0.0.0.0:8080/"
IMPORTS_ENDPOINT = ENDPOINT + "imports"

import_generator = ImportGenerator()
ig = import_generator


@pytest.mark.parametrize("request_body", incorrect_relatives)
def fail_imports(request_body: str):
    response = requests.post(url=IMPORTS_ENDPOINT, data=request_body)
    assert response.status_code == 400
