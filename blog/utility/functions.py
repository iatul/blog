import random
import string
import datetime
from blog.utility.exceptions import BlogException
from blog.common.data import Data

def generate_random_string(size = 15):
	char_string = string.ascii_lowercase + string.digits
	return ''.join(random.choice(char_string) for i in range(size))


def sanitize_payload(request, type):
    try:
        payload = request.json_body
    except:
        BlogException.exception(400, 'Data not in proper JSON format')         
    payload = lowercase_dict_keys(payload)
    mandatory_fields = Data.service.get(type,None)
    missing_fields = []
    filtered_payload = {}

    for k in mandatory_fields:
        if k in payload:
            filtered_payload[k] = payload[k]
        else:
            missing_fields.append(k)
    if not missing_fields:
        return filtered_payload
    else:
        BlogException.exception(400, 'Mandatory fields missing',missing_fields)


def lowercase_dict_keys(my_dict):  # recursive fn that lowercase key of multi dict
    new_dict = {}
    for key, value in my_dict.items():
        if type(value) == dict:
            value = lowercase_dict_keys(value)
        new_dict[key.lower()] = value
    return new_dict


def process_result(result):
    response = list()
    for res in result:
        if type(res) is not dict:
            res = res.__dict__
        for k, v in res.items():
            if isinstance(v, datetime.date):
                res[k] = v.isoformat(' ')
            if k is "_sa_instance_state":
                res.pop(k)    
        response.append(res)
    return response