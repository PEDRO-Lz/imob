from django.urls import path
from .views import register, user_login, home, index, cadastrar_proprietario, cadastrar_imovel, listar_imoveis, excluir_conta, listar_imoveis_usuario
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', index, name='base'),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='base'), name='logout'),
    path('home/', home, name='home'),
    path('cadastrar_proprietario/', cadastrar_proprietario, name='cadastrar_proprietario'),
    path('cadastrar_imovel/', cadastrar_imovel, name='cadastrar_imovel'),
    path('listar_imoveis/', listar_imoveis, name='listar_imoveis'),
    path('listar_imoveis_usuario/', listar_imoveis_usuario, name='listar_imoveis_usuario'),
    path('excluir_conta/', excluir_conta, name='excluir_conta'),
]
