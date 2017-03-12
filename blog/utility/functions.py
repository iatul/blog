import random
import string


def generate_random_string(size = 16):
	char_string = string.ascii_lowercase + string.digits
	return ''.join(random.choice(char_string) for i in range(size))


def general_error_response(status=None, message=None, field=None):
    response = {}
    if status:
        response['status'] = status
    if description:
        response['msg'] = description
    if field:
        response['field'] = field
    return response


def valid_payload(request, **kwargs):
    try:
        payload = request.json_body
    except:
        BlogException.exception(400, 'Data not in JSON format')