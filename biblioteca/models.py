from django.db import models

# Create your models here.

class Cidades(models.Model):
    id_cidade = models.AutoField(primary_key=True)
    nome_cidade = models.CharField(max_length=126)
    class Meta:
        verbose_name_plural = 'Cidades'

    def __str__(self):
        return self.nome_cidade

class Bairros(models.Model):
    id_bairro = models.AutoField(primary_key=True)
    nome_bairro = models.CharField(max_length=126)
    id_cidade_bairro = models.ForeignKey(Cidades, on_delete=models.CASCADE, default=None, null=True)
    class Meta:
        verbose_name_plural = 'Bairros'

    def __str__(self):
        return self.nome_bairro

class Usuarios(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nome_usuario = models.CharField(max_length=126)
    dta_nasc_usuario = models.DateField()
    telefone_usuario = models.CharField(max_length=15)
    email_usuario = models.EmailField(max_length=70)
    numero_usuario = models.CharField(max_length=10)
    logradouro_usuario = models.CharField(max_length=126)
    id_bairro_usuario = models.ForeignKey(Bairros, on_delete=models.CASCADE, default=None, null=True)
    class Meta:
        verbose_name_plural = 'Usuários'

    def __str__(self):
        return self.nome_usuario

class Funcionarios(models.Model):
    id_funcionario = models.AutoField(primary_key=True)
    nome_funcionario = models.CharField(max_length=126)
    dta_nasc_funcionario = models.DateField()
    telefone_funcionario = models.CharField(max_length=15)
    email_funcionario = models.CharField(max_length=70)
    numero_funcionario = models.CharField(max_length=10)
    logradouro_funcionario = models.CharField(max_length=126)
    id_bairro_funcionario = models.ForeignKey(Bairros, on_delete=models.CASCADE, default=None, null=True)
    class Meta:
        verbose_name_plural = 'Funcionários'

    def __str__(self):
        return self.nome_funcionario

class Generos(models.Model):
    id_genero = models.AutoField(primary_key=True)
    nome_genero = models.CharField(max_length=50)
    class Meta:
        verbose_name_plural = 'Gêneros'
    
    def __str__(self):
        return self.nome_genero

class Est_Fisico(models.Model):
    id_est_fisico = models.AutoField(primary_key=True)
    est_fisico = models.CharField(max_length=30)
    class Meta:
        verbose_name_plural = 'Estados Físicos'

    def __str__(self):
        return self.est_fisico

class Livros(models.Model):
    id_livro = models.AutoField(primary_key=True)
    titulo_livro = models.CharField(max_length=100)
    editora_livro = models.CharField(max_length=45)
    autor_livro = models.CharField(max_length=100)
    dta_publicacao_livro = models.DateField()
    qtd_paginas_livro = models.IntegerField()
    id_genero_livro = models.ForeignKey(Generos, on_delete=models.CASCADE, default=None, null=True)
    id_est_fisico_livro = models.ForeignKey(Est_Fisico, on_delete=models.CASCADE, default=None, null=True)
    class Meta:
        verbose_name_plural = 'Livros'

    def __str__(self):
        return self.titulo_livro

class Emprestimos(models.Model):
    id_emprestimos = models.AutoField(primary_key=True)
    dta_emprestimo = models.DateField()
    dta_devolucao = models.DateField()
    id_usuario_emprestimos = models.ForeignKey(Usuarios, on_delete=models.CASCADE, default=None, null=True)
    id_funcionario_emprestimos = models.ForeignKey(Funcionarios, on_delete=models.CASCADE, default=None, null=True)
    id_livro_emprestimos = models.ForeignKey(Livros, on_delete=models.CASCADE, default=None, null=True)
    class Meta:
        verbose_name_plural = 'Empréstimos'

    def __str__(self):
        return self.id_emprestimos

class Tarefas(models.Model):
    id_tarefa = models.AutoField(primary_key=True)
    descricao_tarefa = models.CharField(max_length=100)
    situacao_tarefa = models.BooleanField(default=False)
    class Meta:
        verbose_name_plural = "Tarefas"
    
    def __str__(self):
        return self.id_tarefas