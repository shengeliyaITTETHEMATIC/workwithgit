from django.shortcuts import render
from django.http import HttpResponse
from .models import Statement
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.shortcuts import redirect
from django.conf import settings


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def change_statement(request):
    if not request.user.is_authenticated():
        statements = Statement.objects.all()
        return render(request, 'polls/change_statement.html', {'statements': statements})
    else:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))


def add_statement(request):
    name = request.POST.get('name')
    if name != "":
        data = Statement(name=name)
        data.save()
    statements = Statement.objects.all()
    return render(request, 'polls/change_statement.html', {'statements': statements})


def check_statement(request):
    statements = Statement.objects.all()
    return render(request, 'polls/check_statement.html', {'statements': statements})


def delete_statements(request):
    statements = Statement.objects.all()
    return render(request, 'polls/delete_statement.html', {'statements': statements})


def delete_statement(request):
    id = request.POST.get('ID')
    data = Statement.objects.get(id=id)
    data.delete()
    statements = Statement.objects.all()
    return render(request, 'polls/delete_statement.html', {'statements': statements})


def login(request):
    return render(request, 'polls/login.html', {})


def check_login(request):
    log = request.POST.get('name')
    pas = request.POST.get('pass')
    user = authenticate(username=log, password=pas)
    if user is not None:
        if user.is_active:
            login(request, user)
            return render(request, 'polls/check_statement.html', {})
        else:
            return render(request, 'polls', {})
    else:
        return render(request, 'polls', {})