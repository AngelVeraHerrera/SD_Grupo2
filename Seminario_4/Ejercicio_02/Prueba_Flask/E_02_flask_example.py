# -*- encoding: utf-8 -*-

#Nuestro primer ejemplo
from flask import Flask, render_template
app = Flask(__name__)

#Esto es el router donde indicamos quien responde a cada dirección.
#Vemos coo utilizamos los decoradors en este Ejemplo

@app.route('/')
def index():
    return render_template('application.html')



@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)

@app.route('/users')
def users():
    lalista = ['Miguel', 'Juan', 'Andres']
    return render_template('users.html', lista=lalista)

#Esto lo hacemos para definir que si la función es ejecuta se realice lo siguient
#de esta manera si se utiliza como módulo de otro programa no se ejecutará nada por defecto

if __name__ == '__main__':
    app.run(debug=True)
