"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from filmes.views import FilmeDetailView, FilmesListView, NovoFilmeCreateView, FilmeUpdateView, FilmeDeleteView
from usuarios.views import usuario_view, login_view, logout_view

urlpatterns = [
    path('', FilmesListView.as_view(), name='filmes_list'),
    path('users/', usuario_view, name='usuario'),
    path('admin/', admin.site.urls),
    path('filmes/', FilmesListView.as_view(), name='filmes_list'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('novo_filme/', NovoFilmeCreateView.as_view(), name='novo_filme'),
    path('filme/<int:pk>/', FilmeDetailView.as_view(), name='filme_detail'),
    path('filme/<int:pk>/update/', FilmeUpdateView.as_view(), name='filme_update'),
    path('filme/<int:pk>/delete/', FilmeDeleteView.as_view(), name='filme_delete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
