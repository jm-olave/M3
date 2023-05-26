
#While loop

i = 0 
while i<6:
    print(i)
    i += 1
print(i) 

# for loop
frutas = ["banano","manzana","fresa"]
print(frutas[0])
for x in frutas:
    print(x)

# range()
for j in frutas:
    print("valor")

# range() acotado
y = 0
for y in range(len(frutas)):
    pass

#pass
#break
#continue
ac = 0 
while ac<6:
    ac+=1
    print(ac)
    if ac < 3:
        print(ac)


# dada una lista de 1,100 de Integers, obtenga todos los multiplos de 3 y 5

 
listNUm = list(range(1,101))   
listMulp = []
for bc in listNUm:
    if bc %3 == 0:
        listMulp.append(f'multiplo de 3 :{bc}')
    elif bc %5 == 0:
        listMulp.append(f'multiplo de 5 :{bc}')
print(listMulp)

        
        
        