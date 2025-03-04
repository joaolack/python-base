#!/usr/bin/env python3

"""Imprime a tabuada de 1 a 10"""

# base = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
num = list(range(1, 11))

# Iteração (percorriveis)
for i in num:
    print("Tabuada do:", i)
    for j in num:
        print(i * j)



tabuada=int(input("Tabuada do numero: "))

for count in range(10):
    print("%d x %d = %d" % (tabuada, count+1, tabuada*(count+1)) )




