from src.errors.error_types.http_unprocessable_entity import HttpUnprocessableEntityError
from .tag_creator_validator import tag_creator_validator

class MockResquet:
	def __init__(self, json) -> None:
		self.json = json

	def test_tag_create_validator():
		req = MockResquet(json={"product_code": "12345"})
		tag_creator_validator(req)

	def test_tag_create_validator_with_error():
		req = MockResquet(json={ "product_code": 12345 })
        
		try:
			tag_creator_validator(req)
		except Exception as exception:
			assert isinstance(exception, HttpUnprocessableEntityError)
