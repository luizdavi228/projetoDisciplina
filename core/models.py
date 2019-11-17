from django.db import models

# Livro 
class Livro(models.Model):
    titulo_livro = models.CharField('Titulo', max_length = 255, null = False, blank = False)
    codigo_livro = models.IntegerField('Código', default = 0, null = False, blank = False)
    editora = models.CharField('Editora', max_length = 255,null = False, blank = False)
    nome_primeiro_autor = models.CharField('Primeiro Autor', max_length = 255,null = False, blank = False)
    nome_segundo_autor = models.CharField('Segundo Autor', max_length = 255,null = False, blank = False)
    ano_publicacao = models.IntegerField('Ano de Publicação', default = 0, null = False, blank = False)
    localizacao_estante = models.CharField('Localização',max_length = 255,null = False, blank = False)
    tematica_livro = models.CharField('Temática', max_length = 255,null = False, blank = False)

    class Meta:
        verbose_name = 'Livro'
        verbose_name_plural = 'Livros'

    def __str__(self):
        return self.titulo_livro

class Emprestimo(models.Model):
    data_emprestimo = models.DateField('Data do Empréstimo', null = False)
    matricula_emprestado = models.CharField('Matrícula', max_length = 255,null = False, blank = False)
    data_devolucao = models.DateTimeField('Data de Devolução', null = False)
    codigo_livro = models.IntegerField('Código', default = 0, null = False, blank = False)

    class Meta:

        verbose_name = 'Emprestimo'
        verbose_name_plural = 'Emprestimos'

    def __str__(self):
        return self.matricula_emprestado

class Servidor(models.Model):
    nome = models.CharField('Nome', max_length = 100, null = False, blank = False)
    matricula = models.CharField('Matrícula', max_length = 100, null = False, blank = False)
    email = models.EmailField('E-mail', max_length = 255, null = False, blank = False)
    numero_cpf = models.CharField('CPF', max_length = 50, null = False, blank = False)

    class Meta:

        verbose_name = 'Servidor'
        verbose_name_plural = 'Servidors'

    def __str__(self):
        return self.nome

class Aluno(models.Model):
    nome = models.CharField('Nome', max_length = 100, null = False, blank = False)
    matricula = models.CharField('Matrícula', max_length = 100, null = False, blank = False)
    email = models.EmailField('E-mail', max_length = 255, null = False, blank = False)
    numero_cpf = models.CharField('CPF', max_length = 50, null = False, blank = False)

    class Meta:

        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    def __str__(self):
        return self.nome
