from django.contrib import admin
from apparm.models import Proveedor, Call
from django.utils.html import format_html
# Register your models here.

# PROVEEDOR
class ProveedorAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'telefono', 'email','direccion', 'rrss', 'created_at']
    search_fields = ['nombre', 'telefono', 'email', 'direccion', 'rrss' ]
    list_per_page = 8


admin.site.register(Proveedor, ProveedorAdmin)


#SUPPORT
class CallAdmin(admin.ModelAdmin):
    list_filter = ['Situation']
    list_display = ['user', 'reason', 'option', 'created_at', 'status', '_']
    search_fields = ['user', 'reason', 'option']
    list_per_page = 8

    # Funtion to change the icon (Done, Pending)

    def _(self, obj):
        if obj.Situation == 'Done':
            return True
        else:
            return False
        
    _.boolean = True

    # Function to color the text (Done, Pending)
    def status(self, obj):
        if obj.Situation == 'Done':
            color = '#28a745'
        else:
            color = 'red'
        return format_html('<strong><p style="color: {}">{}</p></strong>'.format(color, obj.Situation))

    status.allow_tags = True

admin.site.register(Call, CallAdmin)