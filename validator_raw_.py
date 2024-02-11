from cerberus import Validator

body = {
	"data": {
	"elemento1": 123.98,
	"elemento2": "olaMundo",
	"elemento3": "123"
	}
}

body_validator = Validator({
	"data": {
		"type": "dict",
		"schema": {
		"elemento1": { "type": "float", "required": True, "empty": False },
		"elemento2": { "type": "string", "required": True, "empty": True },
		"elemento3": { "type": "string", "required": False, "empty": False }
		}
	}
})

response = body_validator.validate(body)

if response is False:
	print(body_validator.errors)
if response is not False:
	print('Body OK')

	# print(response)

	# Seria dessa forma manualmente
	#if "name" in body["data"]: pass
	#if isinstance(body["data"]["name"], int)
