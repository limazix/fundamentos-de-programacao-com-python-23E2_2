# -*- coding: utf-8 -*-

# recursão

# def func():
# condição de parada
#    def func()
# 1, 1, 2, 3, 5, ... -> Fn = Fn-1 + Fn-2


def fibonacci(n: int) -> list:
    """Metodo que gere os primeiros n númros da sequencia de Fibonacci

    param n: quantidade a ser gerada
    type n: int

    return: list com os n primeiros números
    """

    seq = []

    while len(seq) < n:
        if len(seq) < 2:
            seq.append(1)
        else:
            seq.append(seq[-2] + seq[-1])

    return seq


def busca_binaria(seq: list, target: int) -> bool:
    """busca binária

    param seq: sequencia ordenada de valores
    type seq: list

    param target: numero a ser buscado
    type target: int

    return: se o número existe ou não na sequencia
    """

    if len(seq) == 0:
        return False

    if len(seq) == 1:
        return seq[0] == target

    pos_meio = len(seq) // 2

    if seq[pos_meio] > target:
        return busca_binaria(seq[:pos_meio], target)
    else:
        return busca_binaria(seq[pos_meio:], target)


# dado uma frase, como fazer para escrevê-la em ordem contrária
# abcdefg -> gfedcba


def reversao(texto: str) -> str:
    """Método utilizado para reverter uma string

    param texto: Texto a ser revertido
    type texto: str

    return: Texto em ordem reversa
    """

    if len(texto) < 2:
        return texto

    texto_revertido = ''

    for caracter_pos in range(len(texto) - 1, -1, -1):
        texto_revertido += texto[caracter_pos]

    return texto_revertido


def reversao_rec(texto: str) -> str:
    """Método utilizado para reverter uma string utilizando recursão

    param texto: Texto a ser revertido
    type texto: str

    return: Texto em ordem reversa

    abcdefg
    return g + rec(bcdef) + a
    """

    if len(texto) < 2:
        return texto
    else:
        nova_entrada = texto[1:len(texto) - 1]
        return texto[-1] + reversao_rec(nova_entrada) + texto[0]
