from http import HTTPStatus

import pytest

from clients.authentication.authentication_client import get_authentication_client, AuthenticationClient
from clients.authentication.authentication_schema import LoginRequestSchema, LoginResponseSchema
from clients.users.public_users_client import get_public_users_client, PublicUsersClient
from clients.users.users_schema import CreateUserRequestSchema
from tests.conftest import UserFixture
from tools.assertions.authentication import assert_login_response
from tools.assertions.base import assert_status_code
from tools.assertions.schema import validate_json_schema


@pytest.mark.regression
@pytest.mark.authentication
def test_login(
        function_user: UserFixture,
        authentication_client:AuthenticationClient
):
    # Выполняем аутентификацию
    request = LoginRequestSchema(
        email=function_user.email,
        password=function_user.password
    )
    response = authentication_client.login_api(request)
    # Десериализовать JSON-ответ в LoginResponseSchema
    login_response_data = LoginResponseSchema.model_validate_json(response.text)

    # Проверяем статус-код ответа
    assert_status_code(response.status_code, HTTPStatus.OK)
    # Проверяем корректность тела ответа
    assert_login_response(login_response_data)
    # Валидация JSON-схемы
    validate_json_schema(response.json(), LoginResponseSchema.model_json_schema())
