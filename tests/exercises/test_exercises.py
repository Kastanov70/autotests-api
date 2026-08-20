from http import HTTPStatus

import pytest

from clients.errors_schema import InternalErrorResponseSchema
from clients.exercises.exercises_client import ExercisesClient
from clients.exercises.exercises_schema import CreateExerciseRequestSchema, CreateExerciseResponseSchema, \
    GetExerciseResponseSchema, UpdateExerciseRequestSchema, UpdateExerciseResponseSchema, GetExercisesQuerySchema, \
    GetExercisesResponseSchema
from fixtures.courses import CourseFixture
from fixtures.exercises import ExerciseFixture
from tools.assertions.base import assert_status_code
from tools.assertions.exercises import assert_create_exercise_response, assert_get_exercise_response, \
    assert_update_exercise_response, assert_exercise_not_found_response, assert_get_exercises_response
from tools.assertions.schema import validate_json_schema


@pytest.mark.exercises
@pytest.mark.regression
class TestExercises:
    def test_create_exercise(self, exercises_client: ExercisesClient, function_course: CourseFixture):
        # Формируем запрос
        request = CreateExerciseRequestSchema(
            course_id=function_course.response.course.id
        )
        # Отправляем запрос на создание курса
        response = exercises_client.create_exercise_api(request)
        response_data = CreateExerciseResponseSchema.model_validate_json(response.text)

        # Проверяем статус код
        assert_status_code(response.status_code, HTTPStatus.OK)
        # проверяем ответ
        assert_create_exercise_response(request, response_data)

        # Проверяем соответствие JSON-ответа схеме
        validate_json_schema(response.json(), response_data.model_json_schema())

    def test_get_exercise(
            self,
            exercises_client: ExercisesClient,
            function_exercise:ExerciseFixture
    ):
        # Отправляем запрос на получение задания
        response = exercises_client.get_exercise_api(exercise_id=function_exercise.response.exercise.id)
        response_data = GetExerciseResponseSchema.model_validate_json(response.text)

        # Проверяем статус код
        assert_status_code(response.status_code, HTTPStatus.OK)
        # проверяем ответ
        assert_get_exercise_response(function_exercise.response, response_data)

        # Проверяем соответствие JSON-ответа схеме
        validate_json_schema(response.json(), response_data.model_json_schema())

    def test_update_exercise(
            self,
            exercises_client: ExercisesClient,
            function_exercise:ExerciseFixture
    ):
        # Отправляем запрос на обновление задания
        request = UpdateExerciseRequestSchema()
        response = exercises_client.update_exercise_api(
            exercise_id=function_exercise.response.exercise.id,
            request=request
        )
        response_data = UpdateExerciseResponseSchema.model_validate_json(response.text)

        # Проверяем статус код
        assert_status_code(response.status_code, HTTPStatus.OK)
        # проверяем ответ
        assert_update_exercise_response(request=request, response=response_data)

        # Проверяем соответствие JSON-ответа схеме
        validate_json_schema(response.json(), response_data.model_json_schema())

    def test_delete_exercise(
            self,
            exercises_client: ExercisesClient,
            function_exercise:ExerciseFixture
    ):
        # Отправляем запрос на удаление задания
        response = exercises_client.delete_exercise_api(
            exercise_id=function_exercise.response.exercise.id
        )
        # Проверяем статус код
        assert_status_code(response.status_code, HTTPStatus.OK)

        # Отправляем запрос на получение задания
        get_response = exercises_client.get_exercise_api(
            exercise_id=function_exercise.response.exercise.id
        )
        get_response_data = InternalErrorResponseSchema.model_validate_json(get_response.text)

        # Проверяем статус код 404
        assert_status_code(get_response.status_code, HTTPStatus.NOT_FOUND)
        # Проверяем, что в ответе содержится ошибка "Exercise not found"
        assert_exercise_not_found_response(get_response_data)

        # Проверяем, что ответ соответствует схеме
        validate_json_schema(get_response.json(), get_response_data.model_json_schema())

    def test_get_exercises(
            self,
            exercises_client: ExercisesClient,
            function_course:CourseFixture,
            function_exercise:ExerciseFixture
    ):
        query = GetExercisesQuerySchema(course_id=function_course.response.course.id)
        response = exercises_client.get_exercises_api(query=query)
        response_data = GetExercisesResponseSchema.model_validate_json(response.text)

        # Проверяем статус код
        assert_status_code(response.status_code, HTTPStatus.OK)
        # проверяем ответ
        assert_get_exercises_response(response_data, [function_exercise.response.exercise])

        # Проверяем, что ответ соответствует схеме
        validate_json_schema(response.json(), response_data.model_json_schema())
