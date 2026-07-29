from pydantic import BaseModel, EmailStr, Field, SecretStr


class UserSchema(BaseModel):
    """
    Схема данных пользователя.

    Attributes:
        id: Уникальный идентификатор пользователя
        email: Электронная почта пользователя
        last_name: Фамилия пользователя
        first_name: Имя пользователя
        middle_name: Отчество пользователя
    """
    id: str
    email: EmailStr
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")


class CreateUserRequestSchema(BaseModel):
    """
    Схема запроса на создание пользователя.

    Attributes:
        email: Электронная почта пользователя
        password: Пароль пользователя
        last_name: Фамилия пользователя
        first_name: Имя пользователя
        middle_name: Отчество пользователя
    """
    email: EmailStr
    password: str
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")


class CreateUserResponseSchema(BaseModel):
    """
    Схема ответа на создание пользователя.

    Attributes:
        user: Данные созданного пользователя UserShema
    """
    user: UserShema
