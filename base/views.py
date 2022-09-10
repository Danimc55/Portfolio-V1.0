from django.shortcuts import render
from django.http import HttpResponse
from .models import Project
from django.core.mail import send_mail


# Create your views here.
def page(request):
    c = Project.objects.all()[::-1]
    return render(request, 'base/index.html', {'projects': c})

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        subject = "WEBSITE-CONTACT from %s" %name
        data = {
            'name': name,
            'email': email,
            'subject': subject,
            'message': message
        }
        message = '''
        New message: {}

        From: {}
        '''.format(data['message'], data['email'])
        send_mail(data['subject'], message, '', ['danijeltomic@pm.me'])
    return render(request, 'base/contact.html')
