from django.http import Http404
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound
from MainApp.models import Snippet
from django.core.exceptions import ObjectDoesNotExist
from MainApp.forms import SnippetForm

def index_page(request):
    context = {'pagename': 'PythonBin'}
    return render(request, 'pages/index.html', context)


def add_snippet_page(request):
    #Хотим получить чистую форму для заполнения полей
    if request.method == 'GET':
        form = SnippetForm()
        context = {'pagename': 'Добавление нового сниппета',
                   'form': form}
        return render(request, 'pages/add_snippet.html', context)
    
    #Хотим сохранить созданный сниппет
    if request.method == 'POST':
        form = SnippetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("list")
        return render(request,'pages/add_snippet.html',{'form': form})
    
def delete_snippet(request, snippet_id):
    try:
        snippet = Snippet.objects.get(id=snippet_id)
    except ObjectDoesNotExist:
        raise Http404
    else:
        snippet.delete()
        return redirect("list")
    
    
def edit_snippet(request, snippet_id):
    try:
        snippet = Snippet.objects.get(id=snippet_id)
    except ObjectDoesNotExist:
        raise Http404
    #Хотим получить страницу сниппета для изменения полей
    if request.method == 'GET':
        context = {'pagename': 'Редактирование сниппета',
                   'snippet': snippet,
                   'type': 'edit'}
        return render(request, 'pages/snippet_info.html', context)
    
    #Хотим сохранить измененный сниппет
    if request.method == 'POST':
        data_form = request.POST
        snippet.name = data_form['name']
        snippet.lang = data_form['lang']
        snippet.creation_date = data_form['creation_date']
        snippet.code = data_form['code']
        snippet.save()
        return redirect("list")



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
                   'snippet': snippet,
                   'type': 'view'}
        return render(request, 'pages/snippet_info.html', context)
    except ObjectDoesNotExist:
        return HttpResponseNotFound(f'Сниппет не найден')

'''    
def create_snippet(request):
    if request.method == "POST":
        form = SnippetForm(request.POST)
        if form.is_valid():
            orm.save()
            return redirect("list")
        return render(request,'add_snippet.html',{'form': form})
'''

    
