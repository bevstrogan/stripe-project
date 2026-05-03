from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=100, verbose_name='Item Name', help_text='Write Item Name')
    description = models.TextField(max_length=500, verbose_name='Item Description', help_text='Write Item Description')
    price = models.PositiveIntegerField(verbose_name='Item Price', help_text='Write Item Price')
    currency = models.CharField(max_length=3, verbose_name='Item Currency', help_text='Write Item Currency', default='USD')

    class Meta:
        verbose_name = 'Item'
        verbose_name_plural = 'Items'
