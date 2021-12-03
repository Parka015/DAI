from time import time 
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


def funcion_ordenacion(vector, algoritmo):

    respuesta=""

    if algoritmo == "quicksort":

        tiempo_inicial_quick = time() 
        
        vec_quick = quicksort (vector.copy())
        
        tiempo_final_quick = time() 
        
        tiempo_ejecucion_quick = tiempo_final_quick - tiempo_inicial_quick
        
        respuesta = f"Vector SIN Ordenar: {vector} \n"
        respuesta += f" Vector Ordenado: {vec_quick} \n"
        respuesta += f" Tiempo de Quicksort (sg): {tiempo_ejecucion_quick} \n"

    elif algoritmo == "burbuja":

        tiempo_inicial_bur = time() 
        
        vec_burbuja = burbuja (vector.copy())
        
        tiempo_final_bur = time() 
        
        tiempo_ejecucion_bur = tiempo_final_bur - tiempo_inicial_bur
        
        respuesta = f"Vector SIN Ordenar: {vector} \n"
        respuesta += f" Vector Ordenado: {vec_burbuja} \n"
        respuesta += f" Tiempo de Burbuja (sg): {tiempo_ejecucion_bur} \n"
        

    return respuesta
    
    
###################### FIN FUNCIONES AUXILIARES ###############################
###############################################################################