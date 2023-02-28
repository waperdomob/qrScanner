from django.urls import path,include,re_path
from django.conf.urls.static import static
from django.conf import settings
from scanner import views

urlpatterns = [
    path('',views.index, name='inicio'),
    re_path('^leerQR/$', views.leerQR, name='leerQR'),
    #path('leerQR',views.leerQR, name='leerQR'),
    path('generarQR',views.generarQR, name='generarQR'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)