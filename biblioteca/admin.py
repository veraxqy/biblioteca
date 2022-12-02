from django.contrib import admin
from biblioteca.models import Cidades, Bairros, Usuarios, Funcionarios, Generos, Est_Fisico, Livros, Emprestimos
# Register your models here.

admin.site.register(Cidades)
admin.site.register(Bairros)
admin.site.register(Usuarios)
admin.site.register(Funcionarios)
admin.site.register(Generos)
admin.site.register(Est_Fisico)
admin.site.register(Livros)
admin.site.register(Emprestimos)