# Programa para crear un json con todos los nombres de los archivos de los productos orhanizados por su marca

#SE DEBE DE HACER ESTO CADA QUE SE VAYA A SUBIR UNA NUEVA IMAGEN AL GIT, SE ACTUALIZA EL ARCHIVO JSON Y SE SUBE TODO, LAS IMAGENES NUEVAS Y EL JSON YA ACTUALIZADO

#########################  Se importan librerias ###################
import os 
import json
import pathlib
from os import remove
#########################  Fin de importación de librerias #######################

ubicacion = os.getcwd() #Solicitamos la ubicación de donde se encunetra la ruta
# NOTA: Este archivo jsonArchivo.py siempre debe de estar en la carpeta images del proyecto images del git para su funcionamiento correcto

if os.path.isfile(ubicacion + "/archivos.json"): #Validamos que no exista el json llamado archivos.json
	remove(ubicacion + "/archivos.json")#Si lo encuentra, este será eliminado para así actualizarse

contenido = os.listdir(ubicacion + '/productos') #Solicitamos en una lista el nombre de las carpetas dentro de la carpeta productos
dictionario = dict() #Iniciamos un diccionario
diccionarioCarpetas = dict()
n = 0 #Iniciamos un contador
for j in contenido:
	diccionarioCarpetas[n+1] = contenido[n]
	n = n+1
with open(ubicacion + "/carpetas.json","w") as j: #Se crea y se abre un archivo json llamado archivos.json con la indicacion para escribir
	json.dump(diccionarioCarpetas, j) #See ingresa el diccionario al json
n = 0
for i in contenido: #Se crea un for para hacer un guardado del interior de cada carpeta
	archivos = os.listdir('C:/Users/Pfg-D/OneDrive/Escritorio/images/static/Images/productos/'+contenido[n]) #Se crea una lista con todo el contenido de las carpetas en cuestion
	dictionario[contenido[n]] = archivos #Se agrega la lista anterior en la posision de la carpeta principal para su separacion entre marcas
	n = n+1 #Incrementamos el contador
	#Y se reinicia el for hasta que ya haya terminado con todas las carpetas de productos

with open(ubicacion + "/archivos.json","w") as j: #Se crea y se abre un archivo json llamado archivos.json con la indicacion para escribir
	json.dump(dictionario, j) #See ingresa el diccionario al json