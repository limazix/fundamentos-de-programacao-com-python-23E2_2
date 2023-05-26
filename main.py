# -*- coding: utf-8 -*-

# Funções Conhecidas

# print("Hello World!")  Escreve o conteúdo no console
# type() definir o tipo do conteúdo passado
# len() número de itens
# input() entrada de dados do console
# format() formatar uma string combinando texto e variáveis
# range(start, stop, step) percorre todos os valores entre start e stop pulando a cada step
# enumerate()

# 6 - Listas

# lista é um tipo str, int -> list
l = list()
l = []

l = [1, 4, 7, 9]
l = [1, 'oi', 3.5, [5, 7]]
m = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]

# estruturas

# fila
# append()

f = list()
f.append(1)
f.append(2)
f.append(3)
#print(f.index(4))

# pilha

# pop
#
p = list()

p.append(1)
p.append(2)
p.append(3)
# print(p.pop(), p)

last = p[-1]

# ordenação
# sort

l = [7, 9, 4, 5, 8, 41]
l.sort(reverse=True)
# print(l)

l = ['7', '9', '4', '5', '8', '41']
l.sort()
# print(l)

s = 'olá mundo!'
l = s.split(' ')
# print(l)

n = ['x', 'bruno', 'igor']
n.sort(reverse=True)
# print(n)

# print(len(n))

# combinação

# l += n -> l = l + n
l.extend(n)
# print(n, l)

# mutação
l.append('x')
# print(l)

idx = l.index('x')
# l[idx] = 'tamara'
l.insert(idx, 'tamara')  # ñ substitui
# print(idx, l)

# Viagem Escolar

# input
## custo -> 50 - 50000
## pct de estudantes no branch por ano -> 0-1
## num de estudantes no brunchh -> 4 - 2000

# output
## sim
## não


def scholar_trip():
    custo = input('Qual é o custo da viagem: ')
    pct_por_ano = input(
        'Qual é o percentual de cada ano que foi ao brunch sepparado por espaço (numeros entre 0-100): '
    )
    num_estudaantes = input(
        'Qual foi o número total de estudantes que foram aao brunch: ')

    # ajustar os tipos doo input
    custo = float(custo)
    num_estudaantes = int(num_estudaantes)
    pct_por_ano = [float(val) for val in pct_por_ano.split(' ')]

    if len(pct_por_ano) != 4:
        raise Exception(
            "É esperado 4 enntradass correspondendo aos percentuais por ano!")

    pct_total = 0
    for pct in pct_por_ano:
        pct_total += pct

    if pct_total != 100:
        raise Exception(
            "A soma de todos os percentuais deveria ser igual a 100")

    fundo = 0
    for idx, pct in enumerate(pct_por_ano):
        if idx == 0:
            fundo += pct * num_estudaantes * 12 / 100
        elif idx == 1:
            fundo += pct * num_estudaantes * 10 / 100
        elif idx == 2:
            fundo += pct * num_estudaantes * 7 / 100
        else:
            fundo += pct * num_estudaantes * 5 / 100

    if fundo / 2 >= custo:
        print('sim')
    else:
        print('não')


# scholar_trip()

# Bubble Sort
# [5, 7, 9, 3, 2, 10, 15]
# [2, 3, 5, 7, 9, 10, 15]

l = [5, 7, 9, 3, 3, 2, 10, 15]


def bubble_sort(l: list) -> list:
    l_sorted = []
    for i, item1 in enumerate(l):
        if len(l_sorted) == 0:
            l_sorted.append(item1)
            continue
        for j, item2 in enumerate(l_sorted):
            if j + 1 == len(l_sorted):
                l_sorted.append(item1)
                break
            elif item1 > item2:
                continue
            elif item1 <= item2:
                l_sorted.insert(j, item1)
                break
    return l_sorted


# print(bubble_sort(l))

# quick sort e merge sort

# dado um número inteiro ache a soma de todos os multiplos de 3 e 5.
# se o número for negativo ou 0 a função deve retornar 0


def multiplo(numero):
    contador = 0

    if numero <= 0:
        return 0

    for val in range(0, numero + 1, 3):
        contador += val
        print(3, val, contador)

    print('---------------')
    for val in range(0, numero + 1, 5):
        if val % 3 == 0:
            continue
        contador += val
        print(5, val, contador)

    return contador


# print(multiplo(3))

# uma lista com os indices dos 2 numeros que somados deem o número de entrada


def indices(lista: list, target: int) -> list:

    for idx, item1 in enumerate(lista):
        for jdx, item2 in enumerate(lista):
            if idx == jdx:
                continue
            if item1 + item2 == target:
                return [idx, jdx]


# print(indices([1234,5678,9012], 14690))


def jogo_de_matematica(entrada: str) -> int:
    """
    Este método é utilizado para um jogo matemático onde é passada uma string contendo um número, seguido por uma letra e por um outro número. Se a letra for maiúscula, deve-se subtrair o primeiro dígito do segundo. Se a letra for minúscula, deve-se somar ambos os dígitos e se os DÍGITOS forem iguais, deve-se desconsiderar a letra e mostrar o produto entre os dois dígitos.
    
    param entrada: sequencia de tres algarismos compostos por número, letra e número
    type entrada: str

    return: inteiro segundo as regras do jogo
    
    """
    if len(entrada) > 3:
        raise Exception("Entrada inválida!")

    letra = entrada[1]

    if entrada[0] == entrada[2]:
        return int(entrada[0]) * int(entrada[2])
    elif letra == letra.upper():
        return int(entrada[2]) - int(entrada[0])
    else:
        return int(entrada[0]) + int(entrada[2])
