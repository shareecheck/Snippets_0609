from django.http import Http404
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound
from MainApp.models import Snippet
from django.core.exceptions import ObjectDoesNotExist

def index_page(request):
    context = {'pagename': 'PythonBin'}
    return render(request, 'pages/index.html', context)


def add_snippet_page(request):
    context = {'pagename': 'Добавление нового сниппета'}
    return render(request, 'pages/add_snippet.html', context)


def snippets_page(request):
    snippets = Snippet.objects.all()
    context = {'pagename': 'Просмотр сниппетов',
               'snippets': snippets,
               'snippets_amount': len(snippets)}
    return render(request, 'pages/view_snippets.html', context)

def snippet_info_page(request, snippet_id):
    try:
        snippet = Snippet.objects.get(id=snippet_id)
        context = {'pagename': 'Информация о сниппете',
                   'snippet': snippet}
        return render(request, 'pages/snippet_info.html', context)
    except ObjectDoesNotExist:
        return HttpResponseNotFound(f'Сниппет не найден')

    
