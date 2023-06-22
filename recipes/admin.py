from django.contrib import admin

from .models import Category,New_ship

class CategoryAdmin(admin.ModelAdmin):
    ...

@admin.register(New_ship)
class New_shipAdmin(admin.ModelAdmin):
    ...

admin.site.register(Category, CategoryAdmin)
