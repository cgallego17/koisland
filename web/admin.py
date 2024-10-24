from django.contrib import admin
from .models import *

# Register your models here.
class MenuAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'url', 'orden', 'visible')  # Campos que se mostrarán en la lista del admin
    list_filter = ('visible', )  # Filtros por visibilidad y padre
    search_fields = ('nombre',)  # Habilita la búsqueda por nombre
    ordering = ('orden',)  # Ordena automáticamente por el campo 'orden'
    
    # Esto permite seleccionar submenús de manera más sencilla en el admin
    fieldsets = (
        (None, {
            'fields': ('nombre', 'url', 'orden', 'visible', )
        }),
    )
    
# Registra el modelo en el admin
admin.site.register(Menu, MenuAdmin)

# Registra el modelo en el admin
admin.site.register(Proyectos)