from pydantic import BaseModel, Field, EmailStr

from tools.fakers import fake


class TokenSchema(BaseModel):
    """
    Описание модели аутентификационных токенов.
    """
    token_type: str = Field(alias='tokenType')
    access_token: str = Field(alias='accessToken')
    refresh_token: str = Field(alias='refreshToken')


class LoginRequestSchema(BaseModel):
    """
    Описание модели запроса на аутентификацию.
    """
    email: str = Field(default_factory=fake.email)  # Добавили генерацию случайного email
    password: str = Field(default_factory=fake.password)  # Добавили генерацию случайного пароля


class LoginResponseSchema(BaseModel):
    """
    Описание модели ответа аутентификации.
    """
    token: TokenSchema


class RefreshRequestSchema(BaseModel):
    """
    Описание модели запроса для обновления токена.
    """
    refresh_token: str = Field(alias="refreshToken", default_factory=fake.sentence)
