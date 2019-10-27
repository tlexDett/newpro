from django.shortcuts import render
from django.http import HttpResponse
from urllib.parse import parse_qsl
from .models import Service

# Create your views here.
def home(req):
    return render(req, 'myapp/home.html')

def index(req):
    if req.method == 'POST':
        post = req.POST
        s = Service()
        s.icon = post['icon']
        s.title = post['title']
        s.detail = post['detail']
        s.save()
        services = Service.objects.all()
        print(services)
        return render(req, 'myapp/index.html', { 'services': services })
    else:
        services = Service.objects.all()
        print(index)
        return render(req, 'myapp/index.html', { 'services': services })
