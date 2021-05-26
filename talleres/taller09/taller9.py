
archivo =   open('usda-dc-directory.csv', 'r') #Cargar el archivo, r es read

texto_del_archivo = archivo.read() #Leer el archivo

archivo.close() #Cerrar el archivo

separar_linea = texto_del_archivo.split("\n")

tabla_hash = dict()

for line in separar_linea:
    columnas = line.split(",") #Separar las lineas que estan separadas por comas
    apellido = columnas[0] #La columna apellido sera la 0, ver el csv
    nombre = columnas[1] 
    telefono = columnas[3]
    tabla_hash[nombre+" "+apellido] = telefono #El diccionario, en este caso tabla de hash,
                                               #tendra de llave el nombre y apellido y de valor
                                               #tendra el teléfono
    
for nombre_y_apellido in tabla_hash:    #Recorre el diccionario
    print(nombre_y_apellido + ": " + tabla_hash[nombre_y_apellido]) #Para el nombre_y_apellido(key),
                                                                    #mostrar su valor