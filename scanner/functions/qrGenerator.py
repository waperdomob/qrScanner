import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import CircleModuleDrawer, GappedSquareModuleDrawer
import argparse
import os
 
# Preparamos el formato para el código QR
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
 
# Obtenemos el valor del código QR, o bien por parámetro o bien pidiéndolo al usuario
parser = argparse.ArgumentParser()
parser.add_argument("-d", "--dato", type=str, 
    help="Dato con el que se generará el código QR (URL, texto, ...)")
parser.add_argument("-t", "--tipo", type=str, 
    help="Tipo de QR [círculo, cuadrado, Barra_Vertical, Barra_Horizontal, redondeado, Cuadrado_Grande]")
parser.add_argument("-i", "--imagen", type=str, 
    help="Ruta y nombre de fichero de imagen .png con QR que se generará")
args = parser.parse_args()
 
# Obtenemos el parámetro -d (dato)
if args.dato:
    valorQR = args.dato
else:
    valorQR = input("Introduzca el valor del código QR: ")
 
# Obtenemos el parámetro -t (tipo)
if args.tipo:
    tipoQR =  args.tipo
else:
    tipoQR = 'cuadrado'
tipoQR = tipoQR.upper()
# Obtenemos el parámetro -i (fichero de imagen QR)
if args.imagen:
    imagenQR = args.imagen
else:
    imagenQR = os.path.dirname(os.path.abspath(__file__)) + '\codigo_qr.png'
 
# Aplicamos el valor al objeto QR
qr.add_data(valorQR)
 
# Establecemos el tipo de QR según el indicado por parámetro -t
if tipoQR == 'CÍRCULO':
    tipoQRC = CircleModuleDrawer()
elif tipoQR == 'CUADRADO':
    tipoQRC = GappedSquareModuleDrawer()

 
# Generamos el código QR y lo almacenamos en el fichero de imagen PNG
img = qr.make_image(image_factory=StyledPilImage, module_drawer=tipoQRC)
f = open(imagenQR, "wb")
img.save(f)