from src.validators.tag_creator_validator import tag_creator_validator
from src.errors.error_types.http_unprocessable_entity import (
    HttpUnprocessableEntityError,
)


class MockRequest:
    def __init__(self, json) -> None:
        self.json = json


def test_tag_creator_validator():
    request = MockRequest(json={"product_code": "12345"})
    tag_creator_validator(request)


def test_tag_creator_validator_with_error():
    request = MockRequest(json={"product_code": 12345})
    try:
        tag_creator_validator(request)
        assert False
    except Exception as exception:
        assert isinstance(exception, HttpUnprocessableEntityError)
