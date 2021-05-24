import pandas as pd
from time import time
from PIL import Image
import os
import shutil

inicio = time()

if not os.path.isdir("Compresion_imagenes"):
    
    os.mkdir("Compresion_imagenes")

    os.mkdir("Compresion_imagenes\\Ganado_enfermo")
    os.mkdir("Compresion_imagenes\\Ganado_sano")
    

def leer_ganado_enfermo(documento_csv):
    
    ganado_enfermo = pd.read_csv(documento_csv)

    print(ganado_enfermo)
    
    
#leer_ganado_enfermo(open('0.csv'))

def leer_ganado_sano(documento_csv):
    
    ganado_sano = pd.read_csv(documento_csv)

    print(ganado_sano)

#leer_ganado_sano(open('01cowburps-promo-mediumSquareAt3X-v2.csv'))
    

def compresion_imagenes(imagen, tipo_ganado, direccion):

    tipo_ganado = tipo_ganado.lower()
    
    file_name = str(imagen) + "_compressed.jpg"
    im = Image.open(direccion)
    #dim = im.size()
    im.save(file_name, optimize = True, quality= 30)
    if tipo_ganado == "ganado_sano":
        shutil.move(file_name, 'Compresion_imagenes\\Ganado_sano')
    
    elif tipo_ganado == "ganado_enfermo":
        shutil.move(file_name, 'Compresion_imagenes\\Ganado_enfermo')
    
    else:
        
        print ('Por favor intentelo de nuevo e introduzca un tipo de ganado válido.')
        return False
    
    
if not os.path.isdir("Ganado"): #Verifica que haya una carpeta con los archivos a comprimir
    print ("Por favor cree una carpeta Ganado, con dos subcarpetas:")
    print ("Ganado_sano y Ganado_enfermo, que contengan las imagenes a comprimir.")
    
else:
    ganado_sano = os.listdir("Ganado\\Ganado_sano")
    ganado_enfermo = os.listdir("Ganado\\Ganado_enfermo")
    
    
    for ganado in ganado_sano:
        ruta_base = "Ganado\\Ganado_sano"
        ruta_ganado = "\\"+str(ganado)
        ruta_rel = ruta_base + ruta_ganado
        
        compresion_imagenes(str(ganado),"ganado_sano",ruta_rel)
        
    for ganado in ganado_enfermo:
        ruta_base = "Ganado\\Ganado_enfermo"
        ruta_ganado = "\\"+str(ganado)
        ruta_rel = ruta_base + ruta_ganado
        
        compresion_imagenes(str(ganado),"ganado_enfermo",ruta_rel)
    
final = time()

total = final - inicio

print(total)