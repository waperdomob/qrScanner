from django.shortcuts import render
from scanner.functions.qrLector import *
import json
from django.db import transaction

from scanner.models import Ingreso
# Create your views here.

def index(request):
    btniInfo = 'Escanear Código QR'
    datos ={}
    return render(request,'index.html', {'datos':datos,'btnInfo':btniInfo})

def leerQR(request):
    data = qrLector()
    
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
    btniInfo = 'Escanear Código QR'
    
    return render(request, 'index.html',{'datos':datos,'btnInfo':btniInfo})