# -*- coding: UTF-8 -*-

from __future__ import unicode_literals

from django.db import models

##
# Representação de um perfil no Django
##
class Perfil(models.Model):

	##
	# Estrutura da tabela de perfis
	# Precisa rodar os migrations
	##
	nome = models.CharField(max_length=255, null=False)
	email = models.CharField(max_length=255, null=False)     
	telefone = models.CharField(max_length=15, null=False)
	nome_empresa = models.CharField(max_length=255, null=False)

	##
	# Convidar um usuario
	##
	def convidar(self, perfil_convidado):
		convite = Convite(solicitante=self, convidado=perfil_convidado).save()

##
# Representação de um convite
##
class Convite(models.Model):

	##
	# Estrutura da tabela de convite\
	# Adiciona um alias convites_feitos e convites_recebidos para o solicitante e convidado
	##
	solicitante = models.ForeignKey(Perfil, related_name="convites_feitos")
	convidado = models.ForeignKey(Perfil, related_name="convites_recebidos")


