#funciones - son bloques de codigo que realiza una tarea especifica y que son reutilizables

#funcion sin parametro ni devolucion de valor
def saludar():
    print ("hola, bienvenidos al curso de python")

# fumcion con parametros
def saludo(nombre):
    print("hola"+nombre+"bienvenidos a clases")
    
# funcion que devuelve valores
def suma(a, b):
    return a + b

#establecer valores por defecto para los parametros de una funcion
def bienvenida(nombre="estudiante"):
    print("bienvenido",nombre)
#funcion con argumentos variables
def sumador(*args):
    return sum(args)

# llamda de funcion
print (sumador(1,2,3,4,5))
print(sumador(4,5,6))

bienvenida()
bienvenida("susana")

resultado = suma(10,20)
print("la suma es:",resultado)