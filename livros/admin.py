from django.contrib import admin

from .models import Category, Livro


class CategoryAdmin(admin.ModelAdmin):
    ...


@admin.register(Livro)
class LivroAdmin(admin.ModelAdmin):
    list_display = ['id', 'titulo',  'publicado', 'author']
    list_display_links = 'titulo', 
    search_fields = 'id', 'titulo', 'description', 'slug', 'preparation_steps',
    list_filter = 'category', 'author', 'publicado',
    list_per_page = 10
    list_editable = 'publicado',
    ordering = '-id',
    prepopulated_fields = {
        "slug": ('titulo',)
    }

admin.site.register(Category, CategoryAdmin)