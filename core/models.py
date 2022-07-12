from tabnanny import verbose
from django.db import models


class Categoria(models.Model):
    descricao = models.CharField(max_length=25)

    def __str__(self):
        return self.descricao


class Editora(models.Model):
    nome = models.CharField(max_length=100)
    site = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.nome


class Autor(models.Model):
    nome = models.CharField(max_length=225)
    email = models.EmailField()

    def __str__(self):
        return f"{self.nome} {self.email}"

    class Meta:
        verbose_name_plural = "Autores"


class Livros(models.Model):
    titulo = models.CharField(max_length=225)
    ISBN = models.CharField(max_length=13)
    quantidade = models.IntegerField()
    preco = models.DecimalField(max_digits=7, decimal_places=2)
    categoria = models.ForeignKey(
        Categoria, on_delete=models.PROTECT, related_name="livros"
    )
    editora = models.ForeignKey(
        Editora, on_delete=models.PROTECT, related_name="livros"
    )

    def __str__(self):
        return f"{self.titulo}"
