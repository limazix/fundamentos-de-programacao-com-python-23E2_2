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