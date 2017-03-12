import pyramid.httpexceptions as exc
from blog.utility.functions import general_error_response


class BlogException:
    @staticmethod
    def exception(code, message, field=None):
        exc.code = code
        json_output = general_error_response(code, message, field)
        raise exc.exception_response(status_code=code, json_body=json_output)
