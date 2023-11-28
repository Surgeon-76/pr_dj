from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.http import HttpRequest, QueryDict, Http404
from django.urls import reverse
from django.template.loader import render_to_string


def index(request):
    # t = render_to_string('women/index.html')
    # return HttpResponse(t)
    return render(request, 'women/index.html')


def about(request):
    return render(request, 'women/about.html')


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