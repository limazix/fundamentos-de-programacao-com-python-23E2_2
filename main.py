# -*- coding: utf-8 -*-

# Funções Conhecidas

print("Hello World!")  # Escreve o conteúdo no console
# type() # definir o tipo do conteúdo passado
# len número de itens


# 2. Strings (https://www.w3schools.com/python/python_strings.asp)
# '' ou "" -> str

x = "hello world!"
t = type(x)
print(x, t)

# 2.1. Combinar

a = "hello"
b = "world!"

x = a + ' ' + b

print(x)

# 2.2. Cortar

print(len(x))
print(x[2:5])

# 2.3. Modificar

x = x.split(' ')
print(x)

# 2.4. Formatar

a = "Bruno"
x = f"Hello {a}!"
print(x)