# -*- coding: utf-8 -*-


import APIyt
import APId

def SubeVideo(url):#Descarga un video a partir de su url y lo sube a la carpeta de dropbox "video_tube"(sino existe la crea)
	APIyt.DescargarVideo(url)
	nombre = APIyt.TituloU(url)
	APId.subir_video(nombre)

def SubeDrop(urlList):#Descarga el primer video de una lista de youtube y lo sube a la carpeta de dropbox "video_tube"(sino existe la crea)
	url=APIyt.ListaDrop(urlList)
	SubeVideo(url)

def SubeLista(urlList):#Descarga la lista completa de videos de youtube dada y lo sube a la carpeta de dropbox "video_tube"(sino existe la crea)
	APIyt.ListaAll(urlList)
	lista = APIyt.ListaUrl(urlList)
	for i in range(0,len(lista)):#Recorre la lista ya descarga los videos 
		nombre = APIyt.TituloU(lista[i])
		APId.subir_video(nombre)


#main
if __name__ == "__main__":

    print "Desea descargar un video o una lista de videos de Youtube? [1.- Un videos 2.- Una lista de videos]"
    opcion = input()

    if(opcion == 1):
    	print "Introduzca la url del video(Entre comillas dobles)"
    	url = input()
    	SubeVideo(url)
    else:
    	print "Puedes descargar el primer video de la lista o la lista completa [1.- Primer video 2.- Lista completa]"
    	opcion = input()
	
    	if(opcion == 1):
    		print "Introduzca la url de la lista(Entre comillas dobles)"
    		url = input()
    		SubeDrop(url)
    	else:
    		print "Introduzca la url de la lista(Entre comillas dobles)"
    		url = input()
    		SubeLista(url)

#SubeLista("https://www.youtube.com/playlist?list=PLs_R8vjfJCvYXhuklwGPUlbcrUMItm-WV")

