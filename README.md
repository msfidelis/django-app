
# Criando o VirtualEnv

* Instalação do Virtualenv

```
$ sudo pip install virtualenv
```

* Iniciando um Virtualenv

```
$ virtualenv NomeDoAmbiente
```

* Entrando o Environment 

```
$ source ./NomeDoAmbiente/bin/activate
```


# Gerando uma migration

* perfis/models.py

```
from __future__ import unicode_literals

from django.db import models

class Perfil(models.Model):

	nome = models.CharField(max_length=255, null=False)
	email = models.CharField(max_length=255, null=False)     
	telefone = models.CharField(max_length=15, null=False)
	nome_empresa = models.CharField(max_length=255, null=False)

```

```
python manage.py makemigrations

Migrations for 'perfis':
  0001_initial.py:
    - Create model Perfil
```

```
python manage.py migrate

Operations to perform:
  Apply all migrations: admin, contenttypes, perfis, auth, sessions
Running migrations:
  Applying perfis.0001_initial... OK
```