from django.shortcuts import render
import os
from django.http import  JsonResponse
from os import remove
from scanner.models import Ingreso

from scanner.functions.qrLector import *
from scanner.functions.camara import *
from scanner.functions.utils import *
# Create your views here.

def index(request):
    btniInfo = 'Escanear Código QR'
    datos ={}
    return render(request,'index.html', {'datos':datos,'btnInfo':btniInfo})

def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

def leerQR(request):
    if is_ajax(request=request):
        imagen = request.POST.get('imagenQR')
        get_report_image(imagen)
        imgs =cv2.imread("imagenQR.png")
        qrDetector = cv2.QRCodeDetector()
        data, bbox, rectifiedImage = qrDetector.detectAndDecode(imgs)
        if len(data)>0:
            if (data):
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
                print(datos)
                remove("imagenQR.png")
                #ing.save()           
            return JsonResponse({'msg':'QR guardado'})
        else:
            return JsonResponse({'msg':'QR no se pudo guardar'})        
        
    return JsonResponse({})



def generarQR(request):
    return render(request, 'generatorQR.html')

        #if data:
        #    listData = data.split('\n')
        #    datos = {
        #        'nombre':listData[1].replace('N:',""),
        #        'curso':listData[2].replace('TITLE:',""),
        #        'ciudad':listData[4].replace('ADDR:',""),
        #        'telefono':listData[5].replace('TEL:',""),
        #        'email':listData[6].replace('EMAIL:',""),
        #    }
        #    ing = Ingreso()
        #    ing.Nombres = listData[1].replace('N:',"")
        #    ing.celular = listData[5].replace('TEL:',"")
        #    ing.ciudad = listData[4].replace('ADDR:',"")
        #    ing.email = listData[6].replace('EMAIL:',"")
        #    ing.industria_id = 1
        #    #ing.save()
        #    
        #return render(request, 'index.html',{'datos':datos,'btnInfo':btniInfo})