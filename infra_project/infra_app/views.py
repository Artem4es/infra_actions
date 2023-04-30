from django.http import HttpResponse


def index(request):
    return HttpResponse('Офигенчик, а не деплой!')


def second_page(request):
    return HttpResponse('А это вторая страница!')
