from http import HTTPStatus

from fastapi.testclient import TestClient

from fast_zero.app import app


def test_root_deve_retornar_ok_e_ola_mundo():
    client = TestClient(app)  # Arrage(organização)

    response = client.get('/')  # Act

    assert (
        response.status_code == HTTPStatus.OK
    )  # garanta que está funcionado como queremos
    assert response.json() == {'message': 'o palemiras tem mundial'}
