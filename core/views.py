from django.shortcuts import render,redirect, get_object_or_404
from django.contrib import messages
from .models import Livro
from .forms import LivroForm
# Create your views here.

def show_index(request):
    return render(request,'geral/index.html')

def show_home(request):
    return render(request,'home.html')

def show_login(request):
    return render(request,'login.html')

# Livro
def livro_list(request):
    livros = Livro.objects.all()
    contexto = {'livros': livros}
    return render(request, 'livro/livro_list.html',contexto)

def livro_create(request):
    if request.method == 'POST':
        form = LivroForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Livro cadastrado com sucesso')
            return redirect('livro_list')
        else:
            print(form.errors)
    else:
        form = LivroForm()
        contexto = {'form':form}
        return render(request, 'livro/livro_form.html',contexto)

def livro_update(request, codigo_livro):
    livro = Livro.objects.get(codigo_livro = codigo_livro)
    
    if request.method == 'POST':
        form = LivroForm(request.POST, instance=livro)

        if form.is_valid():
            form.save()
            messages.success(request, 'Livro alterado com sucesso')
            return redirect('livro_list')
        else:
            print(form.errors)
    else:
        form = LivroForm(instance=livro)
        contexto = {'form':form}
        return render(request, 'livro/livro_form.html',contexto)

def livro_delete(request, codigo_livro):
    livro = get_object_or_404(Livro, codigo_livro = codigo_livro)

    if request.method == 'POST':
        livro.delete()
        messages.success(request, 'Livro excluído com sucesso')
        return redirect('livro_list')
    else:
        contexto = {'livro':livro}
        return render(request, 'livro/livro_delete.html', contexto)
        
# Usuario