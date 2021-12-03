from flask import Flask, flash ,render_template, request, redirect, url_for, session

from funciones import *
import pickleshare 


paginas = 0
app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'



@app.errorhandler(404)
def rutaErronea(error):
    return	render_template("error.html")
                    
    		

@app.route('/')
@app.route('/index')
def index():

    #Si hay usuario logueado, pasar el usuario
    username = None
    if 'username' in session:
        username = session['username']

    return	render_template("base.html", user= username, paginas = session)


#Función para guardar páginas
@app.before_request
def before_request():
    #Guardamos la url y creamos la variable global de paginas
    url = request.url
    global paginas
    #Cramos expresion regular para que no guarde la url de los elementos de static
    ex = re.compile("(http://localhost:5000/static)+.*")
    #Si es la primera pagina cargada, asignarla y aumentar las paginas
    if(paginas == 0 and not ex.match(url)):
        session['p1'] = url
        paginas = paginas + 1
    #Si ya hay una pagina, poner la nueva pagina como ultima y la otra como penultimo
    elif(paginas == 1 and not ex.match(url)):
        session['p2'] = session['p1']
        session['p1'] = url
        paginas = paginas + 1
    #Si ya hay dos o mas paginas, atrasar las existentes y poner la nueva como última
    elif(paginas == 2 and not ex.match(url)):
        session['p3'] = session['p2']
        session['p2'] = session['p1']
        session['p1'] = url



#Página de registro
@app.route('/registro',methods=['GET','POST'])
def registro():
    #Si hay rellenado el registro, guardarlo
    if (request.method == 'POST'):
        db = pickleshare.PickleShareDB('bd')
        db[request.form['username']] = {'User': request.form['username'],
                                        'Pass': request.form['password'],
                                        'Nombre': request.form['nombre'],
                                        'Apellidos': request.form['apellidos'],
                                        'Email': request.form['email']}

        #Una vez guardado, establecemos esa sesión y vamos a página principal
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return render_template('registro.html',paginas=session)


#Pagina de login
@app.route('/login', methods=['GET','POST'])
def login():
    error = None
    username = None
    #Si se ha logueado, comprobar usuario. Si hay usuario, comprobar contraseña.
    #Si algo falla, mostrar error. Si no, establecer sesión y mandar a pag principal
    if (request.method == 'POST'):
        db = pickleshare.PickleShareDB('bd')
        registrado = request.form['username'] in  db
        if registrado:
            usuario = db[request.form['username']]
            if (usuario['Pass'] == request.form['password']):
                session['username'] = request.form['username']
                return redirect(url_for('index'))
            else:
                error = 'Contraseña incorrecta'
        else:
            error = 'Usuario incorrecto'

    flash('You were successfully logged in')

    return render_template('login.html',error = error, paginas = session)


#Función para el logout
@app.route('/logout', methods=['GET','POST'])
def logout():
    #Si se desloguea, quitar usuario de la sesión y mandar a pag principal
    if request.method == 'POST':
        session.pop('username', None)
    return redirect(url_for('index'))


#Página del perfil
@app.route('/perfil', methods=['GET','POST'])
def perfil():
    #Obtenemos los datos del perfil a traves de la sesión
    username = session['username']
    db = pickleshare.PickleShareDB('bd')
    perfil = db[username]
    return render_template('perfil.html', perfil = perfil, user = username, paginas=session)


#Página de modificación del perfil
@app.route('/modificarPerfil', methods=['GET','POST'])
def modificarPerfil():
    #Obtenemos los datos del perfil y los mandamos para que aparezcan en el formulario
    username = session['username']
    db = pickleshare.PickleShareDB('bd')
    perfil = db[username]
    return render_template('modificarPerfil.html', user= username, perfil = perfil,paginas=session)


#Función para guardar el perfil
@app.route('/guardarPerfil', methods=['GET','POST'])
def guardarPerfil():
    #Si se ha modificado la contraseña, coger la nueva. Si no, quedarnos con la antigua
    if request.form['new_password']:
        p = request.form['new_password']
    else:
        p = request.form['old_password']
    #Creamos nuevo usuario borrando el anterior
    username = session['username']
    db = pickleshare.PickleShareDB('bd')
    del db[username]
    db[request.form['username']] = {'User': request.form['username'],
                                    'Pass': p,
                                    'Nombre': request.form['nombre'],
                                    'Apellidos': request.form['apellidos'],
                                    'Email': request.form['email']}
    #Establecemos sesión del usuario modificado y vamos a página del perfil con nuevos datos
    session['username'] = request.form['username']
    return redirect(url_for('perfil'))

##########################################################################################################
#--------------------------------- Interfaces de los ejercicios -----------------------------------------#
##########################################################################################################


@app.route('/ordena' , methods=['POST', 'GET'])  
def ordena():

    username = None
    if 'username' in session:
        username = session['username']

    resultado = ""

    if request.method == 'POST':

        vector = request.form['lista']
        algoritmo = request.form['algoritmo']
        

        if vector:

            vector = vector.split(",")
            vector = list(map(int, vector))            

            resultado = funcion_ordenacion(vector, algoritmo)
        else:
            resultado = "Parámetro no válido!"


    return	render_template("ordena.html", result=resultado, user= username,  paginas = session)



"Muestra los números primos menores de un número natural dado"
@app.route('/criba', methods=['POST', 'GET'])  
def criba():

    username = None
    if 'username' in session:
        username = session['username']

    respuesta=""

    if request.method == 'POST':

        n = int(request.form['limite'])
    
        lista = list(range(2, n))
        
        i = 0
        while(lista[i]*lista[i] <= n):
            # Mientras el cuadrado del elemento actual sea menor que el ultimo elemento
            for num in lista:
        
                if num % lista[i] == 0 and num != lista[i]:
                    # Si un numero es divisible entre el elemento actual del while
                    # de ser asi, entonces eliminarlo de la lista (esto altera la lista)
                    lista.remove(num)
        
            i += 1 # Incrementa al siguiente elemento de la lista (que ha sido alterada)
        
        respuesta = f"Lista con los números primos menores que {n}: \n {lista}"
    
    return render_template("criba.html", primos=respuesta, user= username, paginas = session) 
    



@app.route('/fibonacci', methods=['POST', 'GET'])   
def fibonacci():

    username = None
    if 'username' in session:
        username = session['username']

    respuesta = ""

    if request.method == 'POST':

        n = int(request.form['n'])

        num_fibo = algoritmo_fibo2(n)

        respuesta += f"El numero de fibonacci de la posición {n} es " + str(num_fibo)

    
    return render_template("fibonacci.html", fibo=respuesta, user= username, paginas = session) 


@app.route('/corchetes', methods=['POST', 'GET'])  
def corchetes():

    username = None
    if 'username' in session:
        username = session['username']

    respuesta = ""

    if request.method == 'POST':

        cadena = request.form['cadena']
    
        valor = 0
        
        respuesta = ""
        
        for elemento in cadena:
            
            if ( elemento == "["):
            
                valor = valor + 1
        
            elif (elemento == "]"):
                valor = valor - 1
                
            else:
                valor = -1
                
            if (valor < 0):
                break
        
        if (valor == 0):
            respuesta = f"La cadena {cadena} ha sido ACEPTADA"
        else:
            respuesta = f"La cadena {cadena} ha sido RECHAZADA"
        
    return  render_template("corchetes.html", result=respuesta, user= username, paginas = session) 


@app.route('/expresionesregulares', methods=['POST', 'GET'])  
def expresionesregulares():

    username = None
    if 'username' in session:
        username = session['username']


    respuesta = ""

    if request.method == 'POST':

        cadena = request.form['expresion']


        respuesta="La palabra introducida es: " + cadena
        if esPalabraConMayuscula(cadena):
            respuesta+=" Es una palabra seguida de una mayúscula."
        elif esEmail(cadena):
            respuesta+=" Es un email."
        elif esTarjetaCredito(cadena):
            respuesta+=" Es un nº de tarjeta de crédito."
        else:
            respuesta+=" No es ni una palabra seguida de una mayúscula, ni un email ni un nº de tarjeta de crédito."

    return render_template("expresion_regular.html", result=respuesta, user= username,  paginas = session)




        
           


