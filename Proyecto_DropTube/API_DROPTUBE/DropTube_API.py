# -*- coding: utf-8 -*-


import APIyt
import APId
import os

client = []
autentificado = False;

#Descarga un video a partir de su url y lo sube a la carpeta de dropbox "video_tube"(sino existe la crea)
def SubeVideo(url):
    global autentificado
    global client

    APIyt.DescargarVideo(url)
    nombre = APIyt.TituloU(url)

    if (not autentificado):
        client = APId.autentificar()
        autentificado = True;

    APId.subir_video(nombre, client)
    os.remove(nombre)

#Descarga el primer video de una lista de youtube y lo sube a la carpeta de dropbox "video_tube"(sino existe la crea)
def SubeDrop(urlList):
	url=APIyt.ListaDrop(urlList)
	SubeVideo(url)

def SubeLista(urlList):#Descarga la lista completa de videos de youtube dada y lo sube a la carpeta de dropbox "video_tube"(sino existe la crea)
#	APIyt.ListaAll(urlList)
	lista = APIyt.ListaUrl(urlList)
	for i in range(0,len(lista)):#Recorre la lista ya descarga los videos 
		SubeVideo(lista[i])


#main

