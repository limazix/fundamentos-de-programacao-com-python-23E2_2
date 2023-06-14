# -*- coding: utf-8 -*-

# TP 4.12 - Escreva um programa que, dados os dados das pessoas que estão na fila, mostre qual posição na fila Aron ocupa.

## Especificação da entrada
# - A 1ª linha de entrada contém um inteiro positivo *N* representando o nº de pessoas que já estavam na fila.
# - As *N* linhas seguintes contêm uma única letra maiúscula cada, representando a cor da camisa da pessoa correspondente.

## Especificação da saída
# Apresente a real posição de Aron na fila.


def get_pos(fila: list) -> int:
    """dados os dados das pessoas que estão na fila, mostre qual posição na fila Aron ocupa

    param fila: lista contendo o número pessoas na fila seguido de suas respectivas cores de camisa
    type fila: list

    return: Posição do Aron na fila
    """

    tamanho = fila[0]
    if tamanho == 0:
        return 1

    pos = 0
    cor_atual = ''
    for cor in fila[0:]:
        if cor != cor_atual:
            cor_atual = cor
            pos += 1

    return pos


def get_pos_rec(pos=1, cor_atual=None):
    cor = input("Digite a cor da camisa: ")

    # condição de parada
    if cor == '':
        return pos

    if cor != cor_atual:
        cor_atual = cor
        pos += 1

    get_pos_rec(pos=pos, cor_atual=cor_atual)
