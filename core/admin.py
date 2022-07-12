from re import M
from django.contrib import admin
from core.models import Categoria, Editora, Autor, Livros

admin.site.register(Categoria)
admin.site.register(Editora)
admin.site.register(Autor)
admin.site.register(Livros)
