from django.contrib import admin

from todo_list.models import TODOO, Category


@admin.register(TODOO)
class TODOOAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'date', 'category', 'due_date')
    list_filter = ('user', 'category__name')
    search_fields = ('title', 'user', 'reminder')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'color')
    search_fields = ('name',)