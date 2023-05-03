# -*- coding: utf-8 -*-

# Funções Conhecidas

# print("Hello World!")  Escreve o conteúdo no console
# type() definir o tipo do conteúdo passado
# len() número de itens
# input() entrada de dados do console

# 3. Entrada de Dados

# 3.1 Fluxo Operracional

# entrada -> processamento -> saida

# print("Qual é seu nome?")

# name = input("Qual é seu nome? \n")

# name = name.split(' ')

# first_name = name[0]
# last_name = name[1]

# response = "Seu nome é {} {}".format(first_name.capitalize(),
#                                      last_name.capitalize())

# print(response)

# val = input("dado: ")

# val = int(val)

# print(type(val))

# 3.2 Contando Palavras - Dado uma entrada no console, imprima quantas palavras foram escritas


def contando_palavras():
    """Método utilizado para contar o número de palavras em uma frase passada pelo prompt"""

    # entrada
    print("Quantas palavras tem na frase?")
    frase = input("Digite uma frase: ")

    # processamento
    frase = frase.split(' ')
    tamanho = len(frase)

    # saída
    resposta = "A frase dada tem {} palavras".format(tamanho)
    print(resposta)


# contando_palavras()

# 3.3 Combinando Nomes - Dado dois nomes com um sobrenome cada, combine parte inicial e final do nome e do sobrenome e imprima o resultado no prompt


def combinando_nomes():

    # entrada
    print("Paracada nome, somente 1 sobrenome é permitido")
    primeiro_nome = input("Digite o primeiro nome: ")
    segundo_nome = input("Digite o segundo nome: ")

    # processamento
    primeiro_nome = primeiro_nome.split(' ')
    segundo_nome = segundo_nome.split(' ')

    nome1 = primeiro_nome[0]
    nome1_tamanho = len(nome1)

    nome2 = segundo_nome[0]
    nome2_tamanho = len(nome2)

    nome_final = nome1[:(1 + nome1_tamanho) // 2] + nome2[nome2_tamanho // 2:]

    sobrenome1 = primeiro_nome[1]
    sobrenome1_tamanho = len(sobrenome1)

    sobrenome2 = segundo_nome[1]
    sobrenome2_tamanho = len(sobrenome2)

    sobrenome_final = sobrenome1[:(1 + sobrenome1_tamanho) //
                                 2] + sobrenome2[sobrenome2_tamanho // 2:]

    # saída
    print(nome_final + ' ' + sobrenome_final)


combinando_nomes()
