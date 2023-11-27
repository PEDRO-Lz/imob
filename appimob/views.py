from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login
from .models import Proprietario, Imovel
from .forms import ImovelForm
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'base.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

@login_required
def home(request):
    return render(request, 'home.html')

@login_required
def cadastrar_proprietario(request):
    if request.method == 'POST':
        cpf = request.POST['cpf']

        proprietario_existente = Proprietario.objects.filter(usuario=request.user).first()

        if not proprietario_existente:
            novo_proprietario = Proprietario.objects.create(usuario=request.user, cpf=cpf)
            return redirect('home')
        else:
            return render(request, 'mensagem_usuario_ja_proprietario.html')

    return render(request, 'cadastrar_proprietario.html')

@login_required
def cadastrar_imovel(request):
    if request.method == 'POST':
        form = ImovelForm(request.POST)
        if form.is_valid():
            imovel = form.save(commit=False)

            imovel.proprietario = Proprietario.objects.get(usuario=request.user)
            imovel.save()

            return redirect('home')

    else:
        form = ImovelForm()

    return render(request, 'cadastrar_imovel.html', {'form': form})
def listar_imoveis(request):
    imoveis = Imovel.objects.all()
    return render(request, 'listar_imoveis.html', {'imoveis': imoveis})

@login_required
def excluir_conta(request):
    if request.method == 'POST':
        request.user.proprietario.imoveis_possuidos.all().delete()
        request.user.proprietario.delete()
        request.user.delete()
        return redirect('logout')  # Redirecionar para logout ou outra página após a exclusão
    return render(request, 'excluir_conta.html')

def listar_imoveis_usuario(request):
    if request.user.is_authenticated:
        imoveis = Imovel.objects.filter(proprietario=request.user)
        return render(request, 'listar_imoveis_usuario.html', {'imoveis': imoveis})
    else:
        pass
