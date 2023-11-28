import math
#função que para calcular o aranjo n p a p
def calcular_arranjo(n,r):
    return math.factorial(n)/math.factorial(n-r)
    #biblioteca math utilizada para calcular o fatorial.

def calcular_permutacao(n):
    return math.factorial(n)

#exemplo de uso:
n = int(input("digite o numero de elementos: "))
r = int(input("digite o numero de combinação: "))

print(f"O Arranjo de {n}, {r} a {r} é {calcular_arranjo(n,r)}" )
print(f"O permutaçã de {n}, {r} a {r} é {calcular_permutacao(n)}" )
