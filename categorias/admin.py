from django.contrib import admin
from .models import Categoria

class ListandoCategoria(admin.ModelAdmin):
    list_display = ('id', 'categ')
    list_display_links = ('id', 'categ')
    search_fields = ('categ',)
    list_per_page = 5

admin.site.register(Categoria, ListandoCategoria)