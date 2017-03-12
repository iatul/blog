import random


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
    return
    if request.method \
        not in DataArray.http_allowed_methods.get(command):
        PayuException.exception(405, 'Not a valid method: %s'
                                % request.method, 'method')