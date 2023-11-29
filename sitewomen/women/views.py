from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.http import HttpRequest, QueryDict, Http404
from django.urls import reverse
from django.template.loader import render_to_string
from django.template.defaultfilters import cut


menu = ['О сайте', 'Добавить статью', 'Обратная связь', 'Войти']

data_db = [
    {'id': 1, 'title': 'Анджелина Джоли', 'content': 'Биография Анджелины Джоли', 'is_published': True},
    {'id': 2, 'title': 'Марго Робби', 'content': 'Биография Марго Робби', 'is_published': False},
    {'id': 3, 'title': 'Джулия Робертс', 'content': 'Биография Джулия Робертс', 'is_published': True},
]


def index(request):
    data = {
        'title': 'Главная страница',
        'menu': menu,
        'posts': data_db,
        }
    return render(request, 'women/index.html', context=data)


def about(request):
    
    return render(request, 'women/about.html', {'title': 'О сайте'})


def categories(request, cat_id):
    return HttpResponse(f"<h1>Статьи по категориям</h1><p>ID: {cat_id}</p>")


def categories_by_slug(request, cat_slug):
    return HttpResponse(f"<h1>Статьи по категориям</h1><p>slug: {cat_slug}</p>")


def archive(request, year):
    if year > 2023:
        # uri = reverse('cats', args=('sport',))
        # return redirect('cats', 'video')
        return redirect(reverse('cats', args=('sport',)))

    return HttpResponse(f"<h1>Архив по годам</h1><p>  {year}</p>")
    # if 1990 <= year <= 2023:
    #     return HttpResponse(f"posts:{year}")
    # raise Http404()


def post_detail(request):
    if request.GET:
        return HttpResponse(" | ".join([f'{k}={v}' for k, v in request.GET.items()]))
    else:
        return HttpResponse("GET is empty")