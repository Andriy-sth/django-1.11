from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth.decorators import login_required


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


@login_required
def userProfile(request):
    user = request.user
    context = {'user': user}
    template = 'profile.html'
    return render(request, template, context)
