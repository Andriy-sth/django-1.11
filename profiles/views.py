from django.shortcuts import render
from django.views.generic import View


# Create your views here.
def home(request):
    context = locals()
    template = 'home.html'
    return render(request, template, context)


class About(View):
    def get(self, request):
        return render(request, 'about.html')
