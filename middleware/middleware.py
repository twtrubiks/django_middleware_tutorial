from django.http import HttpResponse
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)

class SimpleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        logger.warning('---- One-time configuration and initialization. ----')
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        logger.warning('---- 1 ----')
        response = self.get_response(request)
        logger.warning('---- 4 ----')

        # Code to be executed for each request/response after
        # the view is called.

        return response

    # process_view(), process_exception(), process_template_response()
    # special methods to class-based middleware

    def process_view(self, request, view_func, view_args, view_kwargs):
        # process_view() is called just before Django calls the view.
        # It should return either None or an HttpResponse object
        logger.warning('---- 2 ----')
        return None

    def process_exception(self, request, exception):
        # Django calls process_exception() when a view raises an exception
        # It should return either None or an HttpResponse object
        logger.warning('---- exception.args ----')
        return None

    def process_template_response(self, request, response):
        # return TemplateResponse object
        logger.warning('---- 3 ----')
        return response
