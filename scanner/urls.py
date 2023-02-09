from django.urls import path,include,re_path
from django.conf.urls.static import static
from django.conf import settings
from scanner import views

urlpatterns = [
    path('',views.index, name='inicio'),
    path('leerQR',views.leerQR, name='leerQR'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)