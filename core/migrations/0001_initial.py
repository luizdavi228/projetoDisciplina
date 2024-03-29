# Generated by Django 2.2.6 on 2019-11-26 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('matricula', models.CharField(max_length=100, verbose_name='Matrícula')),
                ('email', models.EmailField(max_length=255, verbose_name='E-mail')),
                ('numero_cpf', models.CharField(max_length=50, verbose_name='CPF')),
            ],
            options={
                'verbose_name': 'Usuario',
                'verbose_name_plural': 'Usuarios',
            },
        ),
        migrations.CreateModel(
            name='Emprestimo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_emprestimo', models.DateField(verbose_name='Data do Empréstimo')),
                ('matricula_emprestado', models.CharField(max_length=255, verbose_name='Matrícula')),
                ('data_devolucao', models.DateTimeField(verbose_name='Data de Devolução')),
                ('codigo_livro', models.IntegerField(default=0, verbose_name='Código')),
            ],
            options={
                'verbose_name': 'Emprestimo',
                'verbose_name_plural': 'Emprestimos',
            },
        ),
        migrations.CreateModel(
            name='Livro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo_livro', models.CharField(max_length=255, verbose_name='Titulo')),
                ('codigo_livro', models.IntegerField(default=0, verbose_name='Código')),
                ('editora', models.CharField(max_length=255, verbose_name='Editora')),
                ('nome_primeiro_autor', models.CharField(max_length=255, verbose_name='Primeiro Autor')),
                ('nome_segundo_autor', models.CharField(max_length=255, verbose_name='Segundo Autor')),
                ('ano_publicacao', models.IntegerField(default=0, verbose_name='Ano de Publicação')),
                ('localizacao_estante', models.CharField(max_length=255, verbose_name='Localização')),
                ('tematica_livro', models.CharField(max_length=255, verbose_name='Temática')),
                ('preco', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Preço')),
            ],
            options={
                'verbose_name': 'Livro',
                'verbose_name_plural': 'Livros',
            },
        ),
        migrations.CreateModel(
            name='Servidor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('matricula', models.CharField(max_length=100, verbose_name='Matrícula')),
                ('email', models.EmailField(max_length=255, verbose_name='E-mail')),
                ('numero_cpf', models.CharField(max_length=50, verbose_name='CPF')),
            ],
            options={
                'verbose_name': 'Servidor',
                'verbose_name_plural': 'Servidors',
            },
        ),
    ]
