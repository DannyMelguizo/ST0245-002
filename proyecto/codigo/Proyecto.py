import pandas as pd
from time import time
from PIL import Image
import os
import shutil

inicio = time()

#En el caso de que ya este creada la carpeta donde se almacenaran las imagenes comprimidas no hace nada
if not os.path.isdir("Compresion_imagenes"):  
    
    
    #Crea las carpetas donde se almacenaran las imagenes comprimidas
    os.mkdir("Compresion_imagenes")

    os.mkdir("Compresion_imagenes\\Ganado_enfermo")
    os.mkdir("Compresion_imagenes\\Ganado_sano")
    
#lectura de los archivos csv para el ganado enfermo
def leer_ganado_enfermo(documento_csv):
    
    ganado_enfermo = pd.read_csv(documento_csv)

    print(ganado_enfermo)
    
    
#leer_ganado_enfermo(open('0.csv'))

#lectura de los archivos csv para el ganado sano
def leer_ganado_sano(documento_csv):
    
    ganado_sano = pd.read_csv(documento_csv)

    print(ganado_sano)

#leer_ganado_sano(open('01cowburps-promo-mediumSquareAt3X-v2.csv'))
    
#Metodo para comprimir las imagenes, recibe la imagen, el tipo de ganado, y la ubicacion actual de la imagen a comprimir
def compresion_imagenes(imagen, tipo_ganado, direccion):

    tipo_ganado = tipo_ganado.lower()
    
    #se asigna un nombre para la imagen comprimida
    file_name = str(imagen) + "_compressed.jpg"
    
    #ubica la imagen a comprimir en su ubicacion actual
    im = Image.open(direccion)
    
    #en el caso de querer el tamaño de la imagen
    #dim = im.size()
    
    #comprime la imagen, la variable quality es para definir que tanto se quiere comprimir la imagen, dejarla en 30 para tener buena resolución
    im.save(file_name, optimize = True, quality= 30)
    
    #si el ganado es sano, guarda la imagen en la carpeta de ganado sano
    if tipo_ganado == "ganado_sano":
        shutil.move(file_name, 'Compresion_imagenes\\Ganado_sano')
    
    #si es ganado enfermo, guarda la imagen en la carpeta de ganado enfermo
    elif tipo_ganado == "ganado_enfermo":
        shutil.move(file_name, 'Compresion_imagenes\\Ganado_enfermo')
    
    #en el caso de que no sea enfermo ni sano
    else:
        
        print ('Por favor intentelo de nuevo e introduzca un tipo de ganado válido.')
        return False
    
#Verifica que haya una carpeta con los archivos a comprimir
if not os.path.isdir("Ganado"):
    print ("Por favor cree una carpeta Ganado, con dos subcarpetas:")
    print ("Ganado_sano y Ganado_enfermo, que contengan las imagenes a comprimir.")
    
else:
    ganado_sano = os.listdir("Ganado\\Ganado_sano")
    ganado_enfermo = os.listdir("Ganado\\Ganado_enfermo")
    
    #recorre cada imagen a comprimir en la carpeta ganado sano y se llama al metodo, compresion_image
    for ganado in ganado_sano:
        ruta_base = "Ganado\\Ganado_sano"
        ruta_ganado = "\\"+str(ganado)
        ruta_rel = ruta_base + ruta_ganado
        
        compresion_imagenes(str(ganado),"ganado_sano",ruta_rel)
    
    #recorre cada imagen a comprimir en la carpeta ganado enfermo y se llama al metodo, compresion_image
    for ganado in ganado_enfermo:
        ruta_base = "Ganado\\Ganado_enfermo"
        ruta_ganado = "\\"+str(ganado)
        ruta_rel = ruta_base + ruta_ganado
        
        compresion_imagenes(str(ganado),"ganado_enfermo",ruta_rel)
    
final = time()

total = final - inicio

#captura el tiempo de ejecucion del programa
print(total)
