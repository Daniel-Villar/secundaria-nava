from django.contrib import admin
from .models import AlumnoT,Frase

# Register your models here.
#admin.site.register(AlumnoT)
admin.site.register(Frase)

class ComentarioInt_Line(admin.TabularInline):
    model = Frase
    extra=1

class AlumnoAdmin(admin.ModelAdmin):
    fields=["Apaterno","Amaterno","fecha_nacimiento","fecha_ingreso"]
    list_display=["Apaterno","Amaterno","Nombres"]
    inlines=[ComentarioInt_Line] 
    
admin.site.register(AlumnoT,AlumnoAdmin)

@admin.register(Frase)

class FraseAdmin(admin.ModelAdmin):
    fields=["comentario","Alumno_fk"]
    list_display=["comentarios"]