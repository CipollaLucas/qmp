from django.contrib import admin
from .models import Categoria, Post
# Register your models here.

class CategoriaAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('titulo', 'autor', 'publicado', 'post_categorias')
    ordering = ('publicado', 'autor')
    search_fields = ('titulo', 'contenido', 'autor__username', 'categorias__nombre')
    date_hierarchy = 'publicado'
    list_filter = ('categorias__nombre',)

    #Definimos este método para poder listar las categorias
    def post_categorias(self, obj):
        return ", ".join([c.nombre for c in obj.categorias.all().order_by("nombre")]) #Creamos una lista donde recorra todo lo que hay en "categorias" filtrado por el nombre, y los guardamos
    post_categorias.short_description="Categorías"



    
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Post, PostAdmin)