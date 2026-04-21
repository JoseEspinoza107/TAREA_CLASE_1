# dicccionario -> almacen a pares de clave-valir
mi_diccionario = {'nombre':'Bruno Diaz', 'edad':25,'ciudad': 'La Paz'}
print(mi_diccionario)

#acceder a un valor
print(mi_diccionario['nombre'])
print(mi_diccionario['ciudad'])

#agregar elementos
mi_diccionario['profesion']= 'ingeniero'
print(mi_diccionario)

#eliminar un elemento
del mi_diccionario['ciudad']
print(mi_diccionario)

#obtener claves del diccioanrio
print(mi_diccionario.keys())
#obtener valores del diccioanrio
print(mi_diccionario.values())
#verificar si una clave existe
if 'edad' in mi_diccionario:
    print("clave encontrada")
    
#recorrido de un diccionario
for clave, valor in mi_diccionario.items():
    print("[clave: ]",clave," [Valor:] ",valor)