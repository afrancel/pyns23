#loops de while, repetir hasta que se cumpla una condicion

#caso 1
#variable = 0
#while variable < 5:
#    print(variable)
#    variable += 1

#caso 2
#variable = 0
#while variable < 5:
#    print(variable)
#    if variable == 3:
#        break
#    variable += 1

#caso 3 / da error un ciclo infinito, detener con control+c
#variable = 0
#while variable < 5:
#    print(variable)
#    if variable == 3:
#        continue
#    variable += 1

#caso 4 / solucion, mover el incremento y el print
En este caso, se saltará el 3
variable = 0
while variable < 5:
    variable += 1
    if variable == 3:
        continue
    print(variable)
