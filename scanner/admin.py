from django.contrib import admin
from scanner.models import *
#from import_export.admin import ImportExportModelAdmin
# Register your models here.

class cursoAdmin(admin.ModelAdmin):
    list_display=("id","nombre_curso","ciudad",)

class industriaAdmin(admin.ModelAdmin):
    list_display=("id","industria","curso",)

class inscritoAdmin(admin.ModelAdmin):
    list_display=("id","Nombres","curso",)

class ingresoAdmin(admin.ModelAdmin):
    list_display=("id","Nombres","industria",)

admin.site.register(Cursos,cursoAdmin)
admin.site.register(Industria,industriaAdmin)
admin.site.register(Inscrito,inscritoAdmin)
admin.site.register(Ingreso,ingresoAdmin)