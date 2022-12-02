from dataclasses import field, fields
from django.forms import ModelForm
from .models import Cidades
from .models import Bairros
from .models import Funcionarios
from .models import Usuarios
from .models import Generos
from .models import Est_Fisico
from .models import Livros
from .models import Emprestimos
from .models import Tarefas


class CidadeForm(ModelForm):
    class Meta:
        model = Cidades
        fields = ['id_cidade', 'nome_cidade']

class BairroForm(ModelForm):
    class Meta:
        model = Bairros
        fields = ['id_bairro', 'nome_bairro', 'id_cidade_bairro']

class FuncionarioForm(ModelForm):
    class Meta:
        model = Funcionarios
        fields = ['id_funcionario', 'nome_funcionario', 'dta_nasc_funcionario', 'telefone_funcionario', 'email_funcionario', 'numero_funcionario', 'logradouro_funcionario', 'id_bairro_funcionario']

class UsuarioForm(ModelForm):
    class Meta:
        model = Usuarios
        fields = ['id_usuario', 'nome_usuario', 'dta_nasc_usuario', 'telefone_usuario', 'email_usuario', 'numero_usuario', 'logradouro_usuario', 'id_bairro_usuario']

class GeneroForm(ModelForm):
    class Meta:
        model = Generos
        fields = ['id_genero', 'nome_genero']

class EstFisicoForm(ModelForm):
    class Meta:
        model = Est_Fisico
        fields = ['id_est_fisico', 'est_fisico']

class LivroForm(ModelForm):
    class Meta:
        model = Livros
        fields = ['id_livro', 'titulo_livro', 'editora_livro', 'autor_livro', 'dta_publicacao_livro', 'qtd_paginas_livro', 'id_genero_livro', 'id_est_fisico_livro']

class EmprestimoForm(ModelForm):
    class Meta:
        model = Emprestimos
        fields = ['id_emprestimos', 'dta_emprestimo', 'dta_devolucao','id_usuario_emprestimos', 'id_funcionario_emprestimos', 'id_livro_emprestimos']

class TarefaForm(ModelForm):
    class Meta:
        model = Tarefas
        fields = ['id_tarefa', 'descricao_tarefa', 'situacao_tarefa']