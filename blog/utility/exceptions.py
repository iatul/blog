import pyramid.httpexceptions as exc


class BlogException:
    @staticmethod
    def exception(code, message, field=None):
        exc.code = code
        json_output = {'status' : code, 'msg' : message}
        if field is not None:
        	json_output['field'] = field
        raise exc.exception_response(status_code=code, json_body=json_output)