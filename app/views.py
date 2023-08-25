from django.shortcuts import render
from django.views.generic import TemplateView,ListView
from .forms import Nameform
from .models import Name

# Create your views here.
class HelloView(TemplateView):
    template_name = 'hello.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['hello'] = 'Hello World!'
        return context
    

class NameformView(TemplateView):
    template_name = 'form.html'
    form = Nameform
    def get(self,request,*args,**kwargs):
        context = self.get_context_data(**kwargs)
        context["form"] = self.form
        return render(request,"form.html",context)
    
    def post(self,request,*args,**kwargs):
        form = Nameform(request.POST)
        if form.is_valid():
            form.save()
            context = self.get_context_data(**kwargs)
            context["name"] = form.cleaned_data["name"]
            return render(request,"hello.html",context)
        else:
            context = self.get_context_data(**kwargs)
            context["form"] = form
            return render(request,"form.html",context)

class ListView(ListView):
    template_name = "list.html"
    model = Name