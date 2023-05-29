# funciones creadas por usuario
    # function sumar() suma los valores de param: a,b
def sumar(**a):
    i = 0
    # Ejemplo en clase realizando un while para lectura de kwargs
    while i<len(a):
        keys =list(a.keys())
        values = list(a.values())
        print(keys[i],values[i])
        i+=1
    #iteracion de kwargs realizando un for
    for keys,values in a.items():
        print(keys,values)
    return a # este es el retorno
valor = sumar(b="hola",c ="como", d ="estas",e =3)
print(valor)
