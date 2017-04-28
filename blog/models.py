from django.db import models

'''
class Categoria(models.Model):
    nome = models.CharField('Nome', max_length=100)
    ordem = models.IntegerField('Ordem', blank=False)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['ordem']

    def __str__(self):
        return self.nome
'''


class Item(models.Model):
    nome = models.CharField('Nome', max_length=100)
    ordem = models.IntegerField('Ordem')
    ativo = models.IntegerField('Ativo', default=0)
    # categoria = models.ForeignKey(Categoria, verbose_name='Categoria', related_name='itens')
    convidado = models.CharField('Convidado', max_length=100, blank=True)

    class Meta:
        verbose_name = 'Item'
        verbose_name_plural = 'Itens'
        ordering = ['ordem']

    def __str__(self):
        return self.nome


'''
class Convidado(models.Model):
    nome = models.CharField('Nome', max_length=100)
    item = models.ForeignKey(Item, verbose_name='Item', related_name='convidados')
    created_at = models.DateTimeField('Criado em', auto_now_add=True)

    class Meta:
        verbose_name = 'Convidado'
        verbose_name_plural = 'Convidados'
        ordering = ['created_at']

    def __str__(self):
        return self.nome
'''
