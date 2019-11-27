from django import forms
from .models import Livro

class LivroForm(forms.ModelForm):
    """Form definition for MODELNAME."""

    class Meta:
        """Meta definition for MODELNAMEform."""

        model = Livro
        fields = ('titulo_livro','codigo_livro','editora','nome_primeiro_autor','nome_segundo_autor','ano_publicacao',
        'localizacao_estante','tematica_livro','preco')
