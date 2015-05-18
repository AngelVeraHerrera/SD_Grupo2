# -*- coding: utf-8 -*-

import pafy

def TituloU(url):#Devuelve el titulo del video a partir de una url
	cv=Objvideo(url)
	return cv.title+".webm"

def Titulo(cv):#Devuelve el titulo del video a partir de un objeto 
	return cv.title

def Autor(playlist):#Devuelve el autor de un objeto pafy lista de videos
	return playlist['author']

def Objvideo(url):
	return pafy.new(url)#Crea el objeto pafy con la url de un video

def DescargarVideo(url):#Descarga el video a partir de una url
	cv = Objvideo(url)
	print Titulo(cv)
	video=cv.getbest()#Obtiene el video con mejor calidad del objero cv
	video.download(quiet=False, filepath=video.title + "." + video.extension)#Descarga el video 

def ListaDrop(urlList):#Descargar el primer video de una lista de youtube 
	playlist = pafy.get_playlist(urlList)#Crea un objeto pafy con la url de la lista de YouTube 
	print Autor(playlist)
	return playlist['items'][-(len(playlist['items']))]['pafy'] #Devuelve la url del primer video de la lista de YouTube

def ListaAll(urlList):#Descarga una lista completa de videos de youtube
	playlist = pafy.get_playlist(urlList)#Crea un objeto pafy con la url de la lista de YouTube 
	print Autor(playlist)
	for i in range(0,len(playlist['items'])):#for que recorre toda la lista y descarga video a video
		DescargarVideo(playlist['items'][i]['pafy'])

def ListaUrl(urlList):#Devuelve una lista con las url de todos los videos de la lista dada
	lista = []
	playlist = pafy.get_playlist(urlList)
	for i in range(0,len(playlist['items'])):
		lista.append(playlist['items'][i]['pafy'])
	return lista






