from django.http import HttpResponse
from django.views.generic import TemplateView

def hellowWorld(request):
    return HttpResponse('Hello World!')

class HelloWorld(TemplateView):
    template_name = 'hello.html'
