"""
----------------------------------Métodos--------------------------------
Lista de metodos
  upper()  ---> Convierte en mayusculas un string
  title()------ Convierte la primera letra en Mayuscula
  sort() --------- Ordena los elemementos de una lista  alfabeticamente






-------------------------AQUI EMPIEZA
Cuando tenemos un problema grande lo mejor es dividirlo
 en problemas chicos*/
-----------------------------------------------
python usa la extension .py
-----------------------------------------------------------
#---------VARIABLEES-------------------

 Es un contenedor de valor
composision de variable es .... nombre = "mac"
Las variables en python NO PUEDEN INICIAR CON UN NUMERO pero si ponerlo enotro lugar
 Hay varias variaciones a la hora de declarar una variable
 camelCase --->  nombreCLiente = "juan"
 PascalCase o Capital Camel Case --->  NombreCliente = "juan"
 flatcase --->  nombrecliente = 'juan'
 KebabCase o dash case --->  nombre-cliente = "juan"
 SnakeCase ---> nombre_cliente = "juan" Esta sintaxis es la que MAS SE UTILIZA en Py

 ----------------------TIPO DE DATOS-------------------------
 Strings ->  nombre = "juan"
 Integers -> likes = 201
 Floats -> total_pagar = 100.20
 Boolean - pagado  = True , pagado = False el booleano es en Mayusculas siempre

Python tiene tipado dinamico por ejemplo
 edad = 50
 edad = 51
 edad = "Python"
------------------------------------Funcion y Metodo--------------------------
Funcion: Es un bloque de código diseñado para realizar una actividad
La función muchas veces NO existe y el lenguaje nos deja crear nosotros mismos
para crear una funcion en Python 
            def hola():

Para crear una funcion debemos primero definiir o crear la funcion:
            def hola():
Despues debemos ejecutar la funcion:
            hola()
ERRROR COMUN ES PRIMERO EJECUUTAR LA FUNCION primero y despues definirla por lo
que nos tirara error en la compilación
Es reconmendable identar siempre los def al mismo nivel para no tener errores


-----------------------------------03ARAMETROS y Argumentos
Def hola(nombre):      En este caso lo que esta dentro de la funcion(nombre) es un 
parametro

Si ponemos 2 parametros por ejemplo
        def hola(nombre,puesto): debemos declararla dentro de la funcion
            print (f"soy {nombre} y soy {puesto})
            donde f es para concatenar los parametros/argumentos con strings
            donde {} es donde inyectamos los parametros

Al final si tenemos la funcion ejecutada debemos inyectar los 2 argumetos
    hola('Mac','Nut') el argumento Mac es del parametro "nombre" y el argumento
                        Nut es del parametro "puesto"
    hola('Macoy', 'Inge') aqui seria el argumento Macoy como parametro nombre y 
                        el argumento Inge es el parametro puesto
Al correr el programa nos dara como resultado
    soy Mac y soy Nut
    soy Macoy y soy Inge
Nota: se deben acomodar bien los para metros en la def y los argumentos a la hora de
ejecutar
Mota: si por ejemplo a mi funcion ejecutada le falta un argumento, al momento de
ejecutarlo saltara error por ejemplo
        hola('mac') <<<Le falta el argumento del parametro puesto
Para ello si desconocemos el puesto de mac.... en el parametro puesto declaramos
desconocido en caso de que no sepamos lo antes mencionado

    def hola(nombre, puesto = "Desconocido")
    al final cuando e8jecutamos:
        hola("mac") 
    se imprimira -->  Soy Mac y soy desconocido


-----------------------------------------FUNCIONES QUE RETORNAN VALORES---------------
    No siempre las funciones imprimen un valor ejemplo:
        def hola(planeta):
            return planeta
        satelite = hola('Tierra')
        print (satelite)

----------------------------------------------------Diferencias entre metodos y funciones--
                    FUNCIONES | Metodos
        mostrarNombre(nombre) | nombre.upper() Los metodos son funciones en POO



  ------------------------------------------NUMEROS EN PROGRAMACIón-------------------------------------------
  sirven para mantener resultados , balances, cantidad de likes
   
   cuerpo de operador
   2 + 3 = los numeros son los inputs y  el + es el operador
   se puede restar (-) , sumar(+), dividir (/), multiplicar (*) , potencias (**)
   incrementar += 1 que incrementa +1
   decrementar -= 1 que disminuye -1
------------------------------------------NUMERO Y FUNCIONES---------------
-----------------------------------------TIPS---------------------------
Comentarios para Buenas practicas
Sirven para recordar o para que otra persona entienda nuestro codigo
mantener espacios y orden nos permitirá mas facilidad de lectura
El orden del código esm uy imporante

------------------------------------------------ARREGLOS(ARRAYS)---------------------
En una sola variable permite agrupar muchos datos
En python se conocen como listas
meses = ["Enero","Diciembre","Abril","Marzo"]
meses[1] // Diciembre
La ubicación Diciembre es 1 porque empieza de 0 a 3 en este caso.. abril seria posicion
2 y marzo 3

 """