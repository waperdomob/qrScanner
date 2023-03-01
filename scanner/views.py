from django.shortcuts import render
import cv2
import numpy as np
import base64
from django.http import  JsonResponse
from scanner.models import Ingreso
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt


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

@method_decorator(csrf_exempt)
def leerQR(request):
    if is_ajax(request=request):
        imagen = request.POST.get('imagenQR')
        _ ,str_image = imagen.split('data:image/webp;base64,')
        decoded_data = base64.b64decode(str_image)        
        np_data = np.fromstring(decoded_data,np.uint8)
        img = cv2.imdecode(np_data,cv2.IMREAD_UNCHANGED)
        qrDetector = cv2.QRCodeDetector()
        data, bbox, rectifiedImage = qrDetector.detectAndDecode(img)
        print(data)
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
                #ing.save()           
            return JsonResponse({'msg':data})
        else:
            return JsonResponse({'msg':data})        
        
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