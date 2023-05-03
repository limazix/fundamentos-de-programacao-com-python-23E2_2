# -*- coding: utf-8 -*-


# 1. Operadores (https://www.w3schools.com/python/python_operators.asp)

# 1.1. Tipos de dados

# Conjunto dos números Inteiros [-inf +inf]
1
3
-2
print(3, 2, -5)

print(type(2))

# Conjunto dos números reais 1.1, 2.5...

print('num real', type(2.5))

print(type(2.0))

# 1.2. Variáveis e Atribuições

x = 3
t = type(x)
print(t, x)

# 1.3. Operadores Aritiméticos

# + soma
# - subtração
# / divisão
# *

a = 3
b = 5

x = a + b * b - a / b

t = type(2.0 * 8)
print(t, x)

# ** Potencia
# // floor

x = 2**2

print(x)

x = a + b
x += a

# 1.4. Operadores Lógicos

# or Ou
# and E
# not Oposto

x = bool(1)
y = bool(0)
t = type(x and y)
print(t)

# 1.5. Operadores de Identidade

# is -> é
# is not -> não é

print(type(x) is not type(y))

# 1.6. Operadores de Comparação

# ==
# !=
# >
# <

print(a, b, a > b)

# 1.7. Operadores de Pertencimento

# in -> pertence
# not in -> não pertence

# ver exemplo na sessão 2

# 1.8. Operadores Binários

# & e binária

# | ou binario

# >> shift right

# << shift left

# 000 -> 0
# 001 -> 1
# 010 -> 2
# 010 -> 3
# 100 -> 5
# 110 -> 6
x = a + b
print(x, x << 2, x >> 2)
