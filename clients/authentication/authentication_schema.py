from pydantic import BaseModel, Field, EmailStr


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
    email: EmailStr
    password: str


class LoginResponseSchema(BaseModel):
    """
    Описание модели ответа аутентификации.
    """
    token: TokenSchema


class RefreshRequestSchema(BaseModel):
    """
    Описание модели запроса для обновления токена.
    """
    refreshToken: str
