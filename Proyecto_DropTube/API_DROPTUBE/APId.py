# -*- coding: utf-8 -*-

# Incluye el SDK de Dropbox
import dropbox
import webbrowser
import json
import sys

app_key = "f5u34r9mq9gfbxq"
app_secret = "wuqy333c2xv9qad"

def autentificar():
    access_type = "dropbox"
    webbrowser.get(using=None)
    session = dropbox.session.DropboxSession(app_key, app_secret,access_type)#introduce los parametros necesarios para verificar la 
    request_token = session.obtain_request_token()							 #aplicacion de dropbox
    url = session.build_authorize_url(request_token)
    
    try:
        webbrowser.open_new_tab(url)
    except KeyboardInterrupt:
        pass

    raw_input("Permita el acceso de la aplicacion a Dropbox y pulse <enter>... \n \n")
    access_token = session.obtain_access_token(request_token)
    client = dropbox.client.DropboxClient(session)
    
    data = client.account_info()
    print "Cuenta vinculada -> ", data["display_name"]
    return client;



def subir_video(nombre, client):
    #Abre el fichero 'nombre' ->f
    f = open(nombre, 'rb')
    
    #Todos los videos se guardaran en 'drop_ruta'
    drop_ruta = "/videos_tube/"
    drop_nombre = drop_ruta+nombre
    
    print "Subiendo video..."
    response = client.put_file(drop_nombre, f, False)
    print 'Video subido!!\n'
    

	#EN PHP SUBIR UNA FOTO JPG
	# $file = fopen('files/photo.jpg', 'rb');
	# $size = filesize('files/photo.jpg');
	#
	# $client->uploadfile('/photo.jpg',Dropbox\WriteMode::add(), $file, $size);

