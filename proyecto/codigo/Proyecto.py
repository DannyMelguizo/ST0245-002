import numpy as np
import pandas as pd
from time import time
from PIL import Image
import os
import shutil

inicio = time()

if not os.path.isdir("Compresion_imagenes"): #Verificar si la carpeta donde se almacenaran los datos, ya existe
    
    os.mkdir("Compresion_imagenes") #Crear una carpeta donde se almacenaran los datos

    os.mkdir("Compresion_imagenes\\Ganado_enfermo") #Crear una carpeta donde se almacenaran los datos del ganado enfermo
    os.mkdir("Compresion_imagenes\\Ganado_sano")    #Crear una carpeta donde se almacenaran los datos del ganado sano
    

def leer_ganado_enfermo(documento_csv):
    
    ganado_enfermo = pd.read_csv(documento_csv)

    print(ganado_enfermo)
    
    
#leer_ganado_enfermo(open('0.csv'))

def leer_ganado_sano(documento_csv):
    
    ganado_sano = pd.read_csv(documento_csv)

    print(ganado_sano)

#leer_ganado_sano(open('01cowburps-promo-mediumSquareAt3X-v2.csv'))
    

def compresion_imagenes_perdida(imagen_jpg, tipo_ganado):

    tipo_ganado = tipo_ganado.lower()
    
    file_name = None

    if tipo_ganado == "ganado_sano":
        file_name = str(imagen_jpg) + "_compressed.jpg"
        im = Image.open(imagen_jpg)
        #dim = im.size()
        im.save(file_name, optimize = True, quality= 10)
        shutil.move(file_name, 'Compresion_imagenes\\Ganado_sano')
    
    elif tipo_ganado == "ganado_enfermo":
        file_name = str(imagen_jpg) + "_compressed.jpg"
        im = Image.open(imagen_jpg)
        #dim = im.size()
        im.save(file_name, optimize = True, quality= 10)
        shutil.move(file_name, 'Compresion_imagenes\\Ganado_enfermo')
    
    else:
        
        return 'Por favor intentelo de nuevo e introduzca un tipo de ganado válido.'
    
    
        

#compresion_imagenes_perdida('0.jpg','Ganado_enfermo')
    
final = time()

total = final - inicio

print(total)
