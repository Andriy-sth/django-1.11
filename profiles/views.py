from django.shortcuts import render
from django.views.generic import View


# Create your views here.
def home(request):
    context = {}
    template = 'home.html'
    return render(request, template, context)


class About(View):
    def get(self, request):
        context = {}
        template = 'about.html'
        return render(request, template, context)
