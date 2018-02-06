__author__ = 'jet'

from django.shortcuts import render_to_response
from django import forms
from django.views.decorators.csrf import csrf_exempt

address = [
    {'name': '张三', 'address':'地址一'},
    {'name':'李四', 'address':'地址二'}
    ]


class UserForm(forms.Form):
    username = forms.CharField(label='Username:', max_length=100)
    password = forms.CharField(label='Password:', widget=forms.PasswordInput())

@csrf_exempt
def index(request):
    uf = UserForm()
    return render_to_response('list.html', {'uf': uf})
