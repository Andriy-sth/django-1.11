from django.shortcuts import render
from .forms import contactForm
from django.core.mail import send_mail
from django.conf import settings


# Create your views here.
def contact(request):
    title = 'Contact'
    form = contactForm(request.POST or None)
    context = {'title': title, 'form': form}
    if form.is_valid():
        name = form.cleaned_data['name']
        comment = form.cleaned_data['comment']
        subject = 'Message'
        message = '%s %s' % (comment, name)
        emailFrom = form.cleaned_data['email']
        emailTo = [settings.EMAIL_HOST_USER]
        send_mail(subject, message, emailFrom, emailTo, fail_silently=True)
        title = 'Thanks'
        confirm_message = 'we will get right'
        context = {'title'}

    template = 'contact.html'
    return render(request, template, context)
