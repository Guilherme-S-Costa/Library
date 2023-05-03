from tabnanny import verbose
from trace import Trace
from django.db import models


class Book(models.Model):
    created_at = models.DateField(verbose_name='Criado em', auto_now=True)
    update_at = models.DateField(verbose_name='Editado em', null=True, blank=True)
    deleted_at = models.DateField(verbose_name='Excluido em', editable=False, null=True, blank=True)
    title = models.CharField(max_length=30, verbose_name='Titulo')
    descripition = models.TextField(null=True, blank=True, verbose_name='Descrição')
    category = models.CharField(max_length=100, verbose_name='Categoria')
    pub_date = models.DateField(verbose_name='Data de Publicação', null=True, blank=True)
    version = models.IntegerField(verbose_name='Versão da Edição', default=1)
    publisher = models.CharField(max_length=150, verbose_name='Noma da Editora')
    isbn = models.CharField(max_length=30, verbose_name='Identificador')
    code = models.CharField(max_length=8, verbose_name='Código do Livro', null=True, blank=True, help_text='Código gerado automaticamente')
    author = models.CharField(max_length=100, verbose_name='Nome do Autor')

    class Meta:
        verbose_name = 'Livro'
        verbose_name_plural = 'Livros'

    def __str__(self) -> str:
        return f"{self.pk} | {self.title}"
