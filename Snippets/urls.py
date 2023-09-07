from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from MainApp import views

urlpatterns = [
    path('', views.index_page, name="index"),
    path('snippets/add', views.add_snippet_page, name="add"),
    path('snippets/list', views.snippets_page, name="list"),
    path('delete/<int:snippet_id>', views.delete_snippet, name="delete"),
    #path('snippets/create', views.create_snippet, name="create"),
    path('snippet/<int:snippet_id>/', views.snippet_info_page, name="snippet_info")
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
