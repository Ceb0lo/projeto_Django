from django.http import HttpRequest
from django.views import generic

class PostView(generic.View):
    def get(self, request, *args, **kwargs):
        return HttpRequest('Hello World')
    