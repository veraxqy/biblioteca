"""projeto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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

from biblioteca.views import index
from biblioteca.views import configuracoes

from biblioteca.views import criar_Tarefa
from biblioteca.views import listar_Tarefa

from biblioteca.views import listar_Cidade
from biblioteca.views import criar_Cidade
from biblioteca.views import update_Cidade
from biblioteca.views import delete_Cidade

from biblioteca.views import listar_Bairro
from biblioteca.views import criar_Bairro
from biblioteca.views import update_Bairro
from biblioteca.views import delete_Bairro

from biblioteca.views import listar_Funcionario
from biblioteca.views import criar_Funcionario
from biblioteca.views import update_Funcionario
from biblioteca.views import delete_Funcionario

from biblioteca.views import listar_Usuario
from biblioteca.views import criar_Usuario
from biblioteca.views import update_Usuario
from biblioteca.views import delete_Usuario

from biblioteca.views import listar_Genero
from biblioteca.views import criar_Genero
from biblioteca.views import update_Genero
from biblioteca.views import delete_Genero

from biblioteca.views import listar_EstFisico
from biblioteca.views import criar_EstFisico
from biblioteca.views import update_EstFisico
from biblioteca.views import delete_EstFisico

from biblioteca.views import listar_Livro
from biblioteca.views import criar_Livro
from biblioteca.views import update_Livro
from biblioteca.views import delete_Livro

from biblioteca.views import listar_Emprestimo
from biblioteca.views import criar_Emprestimo
from biblioteca.views import update_Emprestimo
from biblioteca.views import delete_Emprestimo

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='inicial'),
    path('configuracoes/', configuracoes, name='url_configuracoes'),

    path('listar_tarefas/', listar_Tarefa, name='url_listar_tarefas'),
    path('criar_tarefa/', criar_Tarefa, name='url_criar_tarefa'),

    path('listar_funcionarios/', listar_Funcionario, name='url_listar_funcionarios'),
    path('criar_funcionario/', criar_Funcionario, name='url_criar_funcionarios'),
    path('update_funcionario/<int:pk>/', update_Funcionario, name='url_update_funcionario'),
    path('delete_funcionario/<int:pk>/', delete_Funcionario, name='url_delete_funcionario'),

    path('listar_cidades/', listar_Cidade, name='url_listar_cidades'),
    path('criar_cidade/', criar_Cidade, name='url_criar_cidades'),
    path('update_cidade/<int:pk>/', update_Cidade, name='url_update_cidade'),
    path('delete_cidade/<int:pk>/', delete_Cidade, name='url_delete_cidade'),
    
    path('listar_bairros/', listar_Bairro, name='url_listar_bairros'),
    path('criar_bairro/', criar_Bairro, name='url_criar_bairros'),
    path('update_bairro/<int:pk>/', update_Bairro, name='url_update_bairro'),
    path('delete_bairro/<int:pk>/', delete_Bairro, name='url_delete_bairro'),

    path('listar_usuarios/', listar_Usuario, name='url_listar_usuarios'),
    path('criar_usuario/', criar_Usuario, name='url_criar_usuarios'),
    path('update_usuario/<int:pk>/', update_Usuario, name='url_update_usuario'),
    path('delete_usuario/<int:pk>/', delete_Usuario, name='url_delete_usuario'),

    path('listar_generos/', listar_Genero, name='url_listar_generos'),
    path('criar_genero/', criar_Genero, name='url_criar_generos'),
    path('update_genero/<int:pk>/', update_Genero, name='url_update_genero'),
    path('delete_genero/<int:pk>/', delete_Genero, name='url_delete_genero'),

    path('listar_estfisicos/', listar_EstFisico, name='url_listar_estfisicos'),
    path('criar_estfisico/', criar_EstFisico, name='url_criar_estfisicos'),
    path('update_estfisico/<int:pk>/', update_EstFisico, name='url_update_estfisico'),
    path('delete_estfisico/<int:pk>/', delete_EstFisico, name='url_delete_estfisico'),

    path('listar_livros/', listar_Livro, name='url_listar_livros'),
    path('criar_livro/', criar_Livro, name='url_criar_livros'),
    path('update_livro/<int:pk>/', update_Livro, name='url_update_livro'),
    path('delete_livro/<int:pk>/', delete_Livro, name='url_delete_livro'),

    path('listar_emprestimos/', listar_Emprestimo, name='url_listar_emprestimos'),
    path('criar_emprestimo/', criar_Emprestimo, name='url_criar_emprestimos'),
    path('update_emprestimo/<int:pk>/', update_Emprestimo, name='url_update_emprestimo'),
    path('delete_emprestimo/<int:pk>/', delete_Emprestimo, name='url_delete_emprestimo'),
]