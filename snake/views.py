from django.http import HttpResponse
from django.shortcuts import render


def first_page(request):
    text = 'Новый текст'
    a = 'AbC'
    return render(request, './index.html', {
        'a': a,
        'text': text
    })