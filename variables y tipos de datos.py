hola = "Hola Mundo "
a = 1.5
b = 1.5
# valor = int(input("valor:"))
# print(a+b,type(valor) )
lista2 = [ 3,5]

tupla = (("texto",2),(True, lista2))
newdict = dict(tupla)
print(newdict)
lista = [2,"texto",True, hola, lista2]
lista.append(a)
# print(lista)


conjunto = {3, 5, True, 3.4}
dicccionario = {
    "manzana": {
        "semilla": 2,
        "color": "verde"
    },
    "mango": True,
    "banano": lista2
}
dicccionario
print(dicccionario)
