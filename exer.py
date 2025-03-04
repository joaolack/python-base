#!/usr/bin/env python3

"""Exercícios de lógica com Python"""

# Exercício 1
# Faça um programa que peça um número e mostre se ele é positivo ou negativo.
numero = int(input("Digite um número: "))

if numero < 0:
    print("Número negativo")
else:
    print("Número positivo")    

# Exercício 2

sal = float(input("Digite o salário: "))
increase = None



if sal <= 280:
    percentual = "20%"  
    increase = sal * 0.2
    new = increase
elif sal <= 700:
    percentual = "15%"
    increase = sal * 0.15
    new = increase + sal
elif sal <= 1500:
    percentual = "10%"
    increase = sal * 0.1
    new = increase + sal
else:
    percentual = "5%"
    increase = sal * 0.05
    new = increase + sal

print("Salário antes do reajuste: R$", sal)
print("Percentual de aumento aplicado: ", percentual)
print("Valor do aumento: R$", increase)
print("Novo salário após o aumento: R$", new)

