from django.shortcuts import render
from django.db import transaction
from django.views.generic import CreateView
from django.http import StreamingHttpResponse
from scanner.models import Ingreso

from scanner.functions.qrLector import *
from scanner.functions.camara import *
# Create your views here.


def index(request):
    btniInfo = 'Escanear Código QR'
    datos ={}
    return render(request,'index.html', {'datos':datos,'btnInfo':btniInfo})

@gzip.gzip_page
def leerQR(request):
    datos ={}
    btniInfo = 'Escanear Código QR'
    try:
        cam = VideoCamera()
        return StreamingHttpResponse(gen(cam), content_type="multipart/x-mixed-replace;boundary=frame")
    except:
        pass
    return render(request, 'index.html')    
    if data:
        listData = data.split('\n')
        datos = {
            'nombre':listData[1].replace('N:',""),
            'curso':listData[2].replace('TITLE:',""),
            'ciudad':listData[4].replace('ADDR:',""),
            'telefono':listData[5].replace('TEL:',""),
            'email':listData[6].replace('EMAIL:',""),
        }
        ing = Ingreso()
        ing.Nombres = listData[1].replace('N:',"")
        ing.celular = listData[5].replace('TEL:',"")
        ing.ciudad = listData[4].replace('ADDR:',"")
        ing.email = listData[6].replace('EMAIL:',"")
        ing.industria_id = 1
        #ing.save()
        
    return render(request, 'index.html',{'datos':datos,'btnInfo':btniInfo})

def generarQR(request):
    return render(request, 'generatorQR.html')

#class generarQR(CreateView):
#    model = Ingreso
#    template_name='generatorQR.html'