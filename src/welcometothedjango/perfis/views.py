# -*- coding: UTF-8 -*-

from django.shortcuts import render, redirect
from django.http import HttpResponse
from perfis.models import Perfil

##
# Monta uma lista com todos os perfis existentes
##
def index(request):

	#Listar todos:
	perfis = Perfil.objects.all()
	return render(request, 'index.html', {'perfis' : perfis})


##
# Exibir os detalhes do perfil
##
def exibir(request, perfil_id):

	perfil = Perfil.objects.get(id=perfil_id)
	return render(request, 'perfil.html', { "perfil" : perfil })


##
# Gera um convite do usuário logado para o usuário informado
##
def convidar(request, perfil_id):

	perfil_a_convidar = Perfil.objects.get(id=perfil_id)
	perfil_logado = get_perfil_logado()

	perfil_logado.convidar(perfil_a_convidar)
	
	return redirect('index')

##
# Pega o perfil logado no sistema
##
def get_perfil_logado():
	return Perfil.objects.get(id=1)