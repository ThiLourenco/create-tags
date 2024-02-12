from src.errors.error_types.http_unprocessable_entity import HttpUnprocessableEntityError
from src.errors.error_handler import handle_errors

def test_handle_errors_with_http_unprocessable_entity_error():
	error = HttpUnprocessableEntityError("Invalid data")
		
	response = handle_errors(error)
		
	assert response.status_code == 422
		
	assert response.body["errors"][0]["title"] == "UnprocessableEntity"
	assert response.body["errors"][0]["detail"] == "Invalid data"

def test_handle_errors_with_generic_error():
	error = Exception("Unexpected server error")
		
	response = handle_errors(error)
		
	assert response.status_code == 500
		
	assert response.body["errors"][0]["title"] == "Server error"
	assert response.body["errors"][0]["detail"] == "Unexpected server error"
