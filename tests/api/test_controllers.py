import pytest
import requests

from tests.generate_imports import ImportGenerator
from citizen_analyzer.api import controllers

ENDPOINT = "http://0.0.0.0:8080/"


import_generator = ImportGenerator()
ig = import_generator


@pytest.mark.parametrize("request_body", [(ig.generate_import(1).json(), ig.generate_import(1).json()),
                                          ])
def test_imports(request_body: requests.Request):
    endpoint = ENDPOINT + "imports"
    response = requests.post(url=endpoint, data=request_body)
    success_response_data = {"data": {"import_id": 1}}
    assert response.status_code == 201
    assert response.json() == success_response_data

    response = requests.post(url=endpoint, data=request_body)
    success_response_data = {"data": {"import_id": 2}}
    assert response.status_code == 201
    assert response.json() == success_response_data


