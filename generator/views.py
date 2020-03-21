from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.


def home(request):
    return render(request, 'generator/home.html')


def password(request):

    lowercase = 'abcdefghijklmnopqrstuvwxyz'
    uppercase = lowercase.upper()
    numbers = '1234567890'
    special = '!@#~`%$^&*+=.'

    allowed_characters_string = lowercase

    if request.GET.get('uppercase'):
        allowed_characters_string += uppercase

    if request.GET.get('numbers'):
        allowed_characters_string += numbers

    if request.GET.get('special'):
        allowed_characters_string += special

    allowed_characters = list(allowed_characters_string)

    length = int(request.GET.get('length', '16'))

    generated_password = ''

    for x in range(length):
        generated_password += random.choice(allowed_characters)

    return render(request, 'generator/password.html', {
        'password': generated_password
    })


def about(request):
    return render(request, 'generator/about.html')
