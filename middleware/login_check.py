import json
import logging
from logics.models import Employee


class CheckPolicyRequired(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        return self.get_response(request)

    def process_view(self, request, view_func, view_args, view_kwargs):
        print(request.META['PATH_INFO'])
        if(request.META['PATH_INFO'].split('/')[1].lower() == 'login'
        ):
            print('hello')
