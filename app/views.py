from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class HelloView(TemplateView):
    template_name = 'hello.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['hello'] = 'Hello World!'
        return context