import numpy as np
import pandas as pd
from time import time
from PIL import Image
import PIL
import os
import glob


inicio = time()

def leer_ganado_enfermo(documento_csv):
    
    ganado_enfermo = pd.read_csv(documento_csv)

    print(ganado_enfermo)
    
    
#leer_ganado_enfermo(open('0.csv'))

def leer_ganado_sano(documento_csv):
    
    ganado_sano = pd.read_csv(documento_csv)

    print(ganado_sano)

#leer_ganado_sano(open('01cowburps-promo-mediumSquareAt3X-v2.csv'))
    

def compresion_imagenes_perdida(imagen_jpg):

    file_name = 'compressed_image.jpg'
    im = Image.open(imagen_jpg)
    dim = im.size

    im.save(file_name, optimize = True, quality= 10)

#compresion_imagenes_perdida('0.jpg')
    
final = time()

total = final - inicio

print(total)
