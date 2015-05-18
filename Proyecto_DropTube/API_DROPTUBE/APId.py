# -*- coding: utf-8 -*-

# Incluye el SDK de Dropbox
import dropbox
import webbrowser


app_key = "f5u34r9mq9gfbxq"
app_secret = "wuqy333c2xv9qad"


access_type = "dropbox"
session = dropbox.session.DropboxSession(app_key, app_secret,access_type)#introduce los parametros necesarios para verificar la 
request_token = session.obtain_request_token()							 #aplicacion de dropbox
url = session.build_authorize_url(request_token)
webbrowser.open(url, new=1, autoraise=True)#Abre una nueva ventana para solicitar la autorizacion de la aplicacion
raw_input("Presione una tecla para continuar ")
access_token = session.obtain_access_token(request_token)
client = dropbox.client.DropboxClient(session)

print 'link de cuenta: ', client.account_info()



def subir_video(nombre):
	#Abre el fichero 'nombre' ->f
	f = open(nombre, 'rb')

	#Todos los videos se guardaran en 'drop_ruta'
	drop_ruta = "/videos_tube/"
	drop_nombre = drop_ruta+nombre

	response = client.put_file(drop_nombre, f, True)
	print 'uploaded: ', response

	#EN PHP SUBIR UNA FOTO JPG
	# $file = fopen('files/photo.jpg', 'rb');
	# $size = filesize('files/photo.jpg');
	#
	# $client->uploadfile('/photo.jpg',Dropbox\WriteMode::add(), $file, $size);

