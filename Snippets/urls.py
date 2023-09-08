from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from MainApp import views
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index_page, name="index"),
    path('snippets/add', views.add_snippet_page, name="add"),
    path('snippets/list', views.snippets_page, name="list"),
    path('snippets/my_snippets', views.my_snippets, name="my_snippets"),
    path('delete/<int:snippet_id>', views.delete_snippet, name="delete"),
    path('edit/<int:snippet_id>', views.edit_snippet, name="edit"),
    #path('snippets/create', views.create_snippet, name="create"),
    path('snippet/<int:snippet_id>/', views.snippet_info_page, name="snippet_info"),
    path('auth/register', views.create_user, name="register"),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout')

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
