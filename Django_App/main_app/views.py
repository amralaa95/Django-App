
from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from django.http import HttpResponseRedirect

from .models import Users
from .forms import UserForm

def index(request):
    return render(request, 'index.html', {})


def list(request):
    users = Users.objects.order_by('created_at').all()
    context = {'users': users}
    return render(request, 'list.html', context)


def add(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = Users(name=request.POST['name'], email=request.POST['email'])
            user.save()
            return HttpResponseRedirect('/list/')
    else:
        form = UserForm()
    return render(request, 'add.html', {'form': form})