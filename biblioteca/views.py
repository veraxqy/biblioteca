from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse

from .models import Cidades
from .forms import CidadeForm
from .filters import CidadesFilter

from .models import Bairros
from .forms import BairroForm
from .filters import BairrosFilter

from .models import Funcionarios
from .forms import FuncionarioForm
from .filters import FuncionariosFilter

from .models import Usuarios
from .forms import UsuarioForm
from .filters import UsuariosFilter

from .models import Generos
from .forms import GeneroForm
from .filters import GenerosFilter

from .models import Est_Fisico
from .forms import EstFisicoForm
from .filters import Est_FisicoFilter

from .models import Livros
from .forms import LivroForm
from .filters import LivrosFilter

from .models import Emprestimos
from .forms import EmprestimoForm
from .filters import EmprestimosFilter

from .models import Tarefas
from .forms import TarefaForm

# Create your views here.

def index(request):
    data = {}
    data['tarefa'] = Tarefas.objects.all()
    return render(request, 'index.html', data)

def listar_Tarefa(request):
    data = {}
    data['tarefa'] = Tarefas.objects.all()
    return render(request, 'listar_tarefas.html', data)
    
def criar_Tarefa(request):
    data = {}
    form = TarefaForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('inicial')
    data['form'] = form
    return render(request, 'criar_tarefa.html', data)

def configuracoes(request):
    return render(request, 'configuracoes.html')

# CRUD Funcionário:
def listar_Funcionario(request):
    data = {}
    data['funcionario'] = Funcionarios.objects.all()
    data['funcionario_list'] = FuncionariosFilter(request.GET, queryset=data['funcionario'])
    return render(request, 'listar_funcionarios.html', data)

def criar_Funcionario(request):
    data = {}
    form = FuncionarioForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('url_listar_funcionarios')
    data['form'] = form
    return render(request, 'criar_funcionario.html', data)

def update_Funcionario(request, pk):
    data = {}
    funcionario = Funcionarios.objects.get(pk=pk)
    form = FuncionarioForm(request.POST or None, instance=funcionario)

    if form.is_valid():
        form.save()
        return redirect('url_listar_funcionarios')
    data['form'] = form
    return render(request, 'criar_funcionario.html', data)

def delete_Funcionario(request, pk):
    funcionario = Funcionarios.objects.get(pk=pk)
    funcionario.delete()
    return redirect('url_listar_funcionarios')

# CRUD  Cidade:
def listar_Cidade(request):
    data = {}
    data['cidade'] = Cidades.objects.all()
    data['cidade_list'] = CidadesFilter(request.GET, queryset=data['cidade'])
    return render(request, 'listar_cidades.html', data)

def criar_Cidade(request):
    data = {}
    form = CidadeForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('url_listar_cidades')
    data['form'] = form
    return render(request, 'criar_cidade.html', data)

def update_Cidade(request, pk):
    data = {}
    cidade = Cidades.objects.get(pk=pk)
    form = CidadeForm(request.POST or None, instance=cidade)

    if form.is_valid():
        form.save()
        return redirect('url_listar_cidades')
    data['form'] = form
    return render(request, 'criar_cidade.html', data)

def delete_Cidade(request, pk):
    cidade = Cidades.objects.get(pk=pk)
    cidade.delete()
    return redirect('url_listar_cidades')

# CRUD Bairro:
def listar_Bairro(request):
    data = {}
    data['bairro'] = Bairros.objects.all()
    data['bairro_list'] = BairrosFilter(request.GET, queryset=data['bairro'])
    return render(request, 'listar_bairros.html', data)

def criar_Bairro(request):
    data = {}
    form = BairroForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('url_listar_bairros')
    data['form'] = form
    return render(request, 'criar_bairro.html', data)

def update_Bairro(request, pk):
    data = {}
    bairro = Bairros.objects.get(pk=pk)
    form = BairroForm(request.POST or None, instance=bairro)

    if form.is_valid():
        form.save()
        return redirect('url_listar_bairros')
    data['form'] = form
    data['bairro'] = bairro
    return render(request, 'criar_bairro.html', data)

def delete_Bairro(request, pk):
    bairro = Bairros.objects.get(pk=pk)
    bairro.delete()
    return redirect('url_listar_bairros')

# CRUD Usuário:
def listar_Usuario(request):
    data = {}
    data['usuario'] = Usuarios.objects.all()
    data['usuario_list'] = UsuariosFilter(request.GET, queryset=data['usuario'])
    return render(request, 'listar_usuarios.html', data)

def criar_Usuario(request):
    data = {}
    form = UsuarioForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('url_listar_usuarios')
    data['form'] = form
    return render(request, 'criar_usuario.html', data)

def update_Usuario(request, pk):
    data = {}
    usuario = Usuarios.objects.get(pk=pk)
    form = UsuarioForm(request.POST or None, instance=usuario)

    if form.is_valid():
        form.save()
        return redirect('url_listar_usuarios')
    data['form'] = form
    data['usuario'] = usuario
    return render(request, 'criar_usuario.html', data)

def delete_Usuario(request, pk):
    usuario = Usuarios.obejcts.get(pk=pk)
    usuario.delete()
    return redirect('url_listar_usuarios')

# CRUD Gênero:
def listar_Genero(request):
    data = {}
    data['genero'] = Generos.objects.all()
    data['genero_list'] = GenerosFilter(request.GET, queryset=data['genero'])
    return render(request, 'listar_generos.html', data)

def criar_Genero(request):
    data = {}
    form = GeneroForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('url_listar_generos')
    data['form'] = form
    return render(request, 'criar_genero.html', data)

def update_Genero(request, pk):
    data = {}
    genero = Generos.objects.get(pk=pk)
    form = GeneroForm(request.POST or None, instance=genero)

    if form.is_valid():
        form.save()
        return redirect('url_listar_generos')
    data['form'] = form
    data['genero'] = genero
    return render(request, 'criar_genero.html', data)

def delete_Genero(request, pk):
    genero = Generos.objects.get(pk=pk)
    genero.delete()
    return redirect('url_listar_generos')

# CRUD Est_Fisico:
def listar_EstFisico(request):
    data = {}
    data['estfisico'] = Est_Fisico.objects.all()
    data['est_fisico_list'] = Est_FisicoFilter(request.GET, queryset=data['estfisico'])
    return render(request, 'listar_estfisicos.html', data)

def criar_EstFisico(request):
    data = {}
    form = EstFisicoForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('url_listar_estfisicos')
    data['form'] = form
    return render(request, 'criar_estfisico.html', data)

def update_EstFisico(request, pk):
    data = {}
    estfisico = Est_Fisico.objects.get(pk=pk)
    form = EstFisicoForm(request.POST or None, instance=estfisico)

    if form.is_valid():
        form.save()
        return redirect('url_listar_estfisicos')
    data['form'] = form
    data['estfisico'] = estfisico
    return render(request, 'criar_estfisico.html', data)

def delete_EstFisico(request, pk):
    estfisico = Est_Fisico.objects.get(pk=pk)
    estfisico.delete()
    return redirect('url_listar_estfisicos')

# CRUD Livro:
def listar_Livro(request):
    data = {}
    data['livro'] = Livros.objects.all()
    data['livro_list'] = LivrosFilter(request.GET, queryset=data['livro'])
    return render(request, 'listar_livros.html', data)

def criar_Livro(request):
    data = {}
    form = LivroForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('url_listar_livros')
    data['form'] = form
    return render(request, 'criar_livro.html', data)

def update_Livro(request, pk):
    data = {}
    livro = Livros.objects.get(pk=pk)
    form = LivroForm(request.POST or None, instance=livro)

    if form.is_valid():
        form.save()
        return redirect('url_listar_livros')
    data['form'] = form
    data['livro'] = livro
    return render(request, 'criar_livro.html', data)

def delete_Livro(request, pk):
    livro = Livros.objects.get(pk=pk)
    livro.delete()
    return redirect('url_listar_livros')

# CRUD Emprestimo:
def listar_Emprestimo(request):
    data = {}
    data['emprestimo'] = Emprestimos.objects.all()
    data['emprestimo_list'] = EmprestimosFilter(request.GET, queryset=data['emprestimo'])
    return render(request, 'listar_emprestimos.html', data)

def criar_Emprestimo(request):
    data = {}
    form = EmprestimoForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('url_listar_emprestimos')
    data['form'] = form
    return render(request, 'criar_emprestimo.html', data)

def update_Emprestimo(request, pk):
    data = {}
    emprestimo = Emprestimos.objects.get(pk=pk)
    form = EmprestimoForm(request.POST or None, instance=emprestimo)

    if form.is_valid():
        form.save()
        return redirect('url_listar_emprestimos')
    data['form'] = form
    return render(request, 'criar_emprestimo.html', data)

def delete_Emprestimo(request, pk):
    emprestimo = Emprestimos.objects.get(pk=pk)
    emprestimo.delete()
    return redirect('url_listar_emprestimo')