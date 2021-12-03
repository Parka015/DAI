from flask import Flask
app = Flask(__name__)



from time import time 
import random
import re


######################## FUNCIONES AUXILIARES #################################

def burbuja(B):
    A = B.copy()
    for i in range(1,len(A)):
        for j in range(0,len(A)-i):
            if(A[j+1] < A[j]):
                aux=A[j];
                A[j]=A[j+1];
                A[j+1]=aux;
    return A
                
                
#Por revisar

def quicksort(lista):
    izquierda = []
    centro = []
    derecha = []
    if len(lista) > 1:
        pivote = lista[0]
        for i in lista:
            if i < pivote:
                izquierda.append(i)
            elif i == pivote:
                centro.append(i)
            elif i > pivote:
                derecha.append(i)
        #print(izquierda+["-"]+centro+["-"]+derecha)
        return quicksort(izquierda)+centro+quicksort(derecha)
    else:
      return lista
  
#Mucho menos eficiente
"""
def algoritmo_fibo1(num):
    if (num == 1):
        return 0
    elif (num == 2):
        return 1
    else: 
        return algoritmo_fibo1(num-1) + algoritmo_fibo1(num-2)
"""   
  
def algoritmo_fibo2(num):
    
    ultimo, siguiente = 0, 1
    
    cont=1
    
    while cont < num:
        ultimo, siguiente = siguiente, ultimo + siguiente
        cont += 1
    
    return ultimo

def esPalabraConMayuscula(string):
    
    match = re.match(r"[A-Za-z]+\s[A-Z]",string)

    return match  


def esEmail(string):#[a-zA-Z]\w*@ ... +[a-z]
    #[a-zA-Z]\w*@([a-z]+\.)+[a-z]+
    #debo usar search porque sino falla con findall
    match = re.match(r"[a-zA-Z]\w*@([a-z]+\.)+[a-z]+",string)

    return match 
    
def esTarjetaCredito(string):
    #[ -]){4}
    match = re.match(r"([0-9]{4}[ -]){3}[0-9]{4}",string)

    return match 
    
    
###################### FIN FUNCIONES AUXILIARES ###############################
###############################################################################


@app.errorhandler(404)
def rutaErronea(error):

    return	'''
                    <!DOCTYPE html>
                    <html>
                      <head>
                        <meta charset="utf-8">

                        <title>Práctica 1 DAI</title>
                        <meta name="viewport" content="width=device-width, initial-scale=1.0">
                        <meta name="author" content="Pablo Ruiz Mingorance">
                        <link href="/static/style.css" rel="stylesheet" type="text/css" />
                      </head>
                      <body>
                            <div class="Error">
                              <h1 class="error">La url no está definida - ERROR 404 </h1>
                              <img class="imagen" src="/static/img/imagen_error404.jpeg"/>
                            </div>
                      </body>
                    </html>
    			'''



@app.route('/')
def index():
    return	'''
                    <!DOCTYPE html>
                    <html>
                      <head>
                        <meta charset="utf-8">

                        <title>Práctica 1 DAI</title>
                        <meta name="viewport" content="width=device-width, initial-scale=1.0">
                        <meta name="author" content="Pablo Ruiz Mingorance">
                        <link href="/static/style.css" rel="stylesheet" type="text/css" />
                      </head>
                      <body>
                        <div>
                    			<h1>Práctica 1 DAI </h1>
                    			<h2>Ejercicios</h2>
                                <div class="lista">
                        			<ul>
                        				<li><a href="http://localhost:5000/ordena/6,5,2,1,3,10"> Algoritmos de ordenación</a></li>
                        				<li><a href="http://localhost:5000/criba/50"> Criba de Eratóstenes</a></li>
                        				<li><a href="http://localhost:5000/fibonacci/10"> Calculo de n-ésimo elemento en la Sucesión de Fibonacci</a></li>
                        				<li><a href="http://localhost:5000/corchetes/[[[][]]]"> Comprobación de corchetes cerrados correctamente</a></li>
                        				<li><a href="http://localhost:5000/expresionesregulares/1111 2222 3333 4444"> Identificador de pablabras seguidas de un espacio y una mayúscula, de un email y de una tajerta de crédito</a></li>
                                    <li><a href="http://localhost:5000/svg"> Ejercicio opcional SVG</a></li>
                            </ul>

                        </div>
                      </body>
                    </html>
    			'''



@app.route('/ordena/<vector>')  
def ordena(vector):
    #vector = np.random.randint(0,50000,(1,1000))
    #vector = vector[0]
 
    vector = vector.split(",")
    
    vector = list(map(int, vector))
        
    
    tiempo_inicial_quick = time() 
    
    vec_quick = quicksort (vector.copy())
    
    tiempo_final_quick = time() 
     
    tiempo_ejecucion_quick = tiempo_final_quick - tiempo_inicial_quick
    
    respuesta = f"Vector SIN Ordenar: {vector} \n"
    respuesta += f" Tiempo de Quicksort: {tiempo_ejecucion_quick} \n"
    #print (vec_quick)
    
    #print ("\n\n\n",vector)
    
    
    tiempo_inicial_bur = time() 
    
    vec_burbuja = burbuja (vector.copy())
    
    tiempo_final_bur = time() 
     
    tiempo_ejecucion_bur = tiempo_final_bur - tiempo_inicial_bur
    
    respuesta += f" Tiempo de Burbuja: {tiempo_ejecucion_bur} \n"
    respuesta += f" Vector Ordenado: {vec_quick} \n"
    
    return respuesta

a=ordena("2,10,1,3")

"Muestra los números primos menores de un número natural dado"
@app.route('/criba/<int:n>')  
def criba(n):

    #n = int(input("Ingrese un numero: "))
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
    
    return respuesta 
    



@app.route('/fibonacci/<int:n>')  
def fibonacci(n):

    num_fibo = algoritmo_fibo2(n)
    
    #archivo_nuevo = open(f"{n}º_numero_fibonacci.txt","w")
    
    #archivo_nuevo = archivo_nuevo.write(str(num_fibo))
    
    return f"El numero de fibonacci de la posición {n} es " + str(num_fibo)


@app.route('/corchetes/<cadena>') 
def corchetes(cadena):
    
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
        
    return respuesta


@app.route('/expresionesregulares/<cadena>')
def expresionesregulares(cadena):
    c="La palabra introducida es: " + cadena
    if esPalabraConMayuscula(cadena):
        c+=" Es una palabra seguida de una mayúscula"
    elif esEmail(cadena):
        c+=" Es un email"
    elif esTarjetaCredito(cadena):
        c+=" Es un nº de tarjeta de crédito"
    else:
        c+=" No es ni una palabra seguida de una mayúscula, ni un email ni un nº de tarjeta de crédito"
    return c


@app.route('/svg')
def svg():
    
    aleatorio =random.randint(0,2)
    figura = aleatorio
    
    if figura == 0:
        cx = random.uniform(2,8)
        cy = random.uniform(2,8)
        rx = random.uniform(0.1,8)
        ry = random.uniform(0.1,8)
        figura = f"""<ellipse class="fig" cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" color="red"/>"""
        
    elif figura == 1:
        cx = random.uniform(2,8)
        cy = random.uniform(2,8)
        r = random.uniform(0.1,8)
        figura = f"""<circle class="fig" cx="{cx}" cy="{cy}" r="{r}" />"""
        
    elif figura == 2:
       x = random.uniform(2,8)
       y = random.uniform(2,8)
       height = random.uniform(0.1,8)
       width = random.uniform(0.1,8)
       figura = f"""<rect class="fig" x="{x}" y="{y}" height="{height}" width="{width}" />"""
      
    colores = ["blue","yellow", "aqua", "salmon", "tomato", "orange", "lightgreen"]    
    color= colores[random.randint(0,len(colores)-1)]
    

    return """
                <svg viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg" >
                    <title>Estructura basica del SVG</title>
                    <style>
                        .fig {fill: """ f""" {color}""" + """}  
                    </style>
                """+ f"""
                
                {figura}
            
                </svg>
                """
        
           


