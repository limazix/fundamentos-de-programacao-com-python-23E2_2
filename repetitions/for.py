# -*- coding: utf-8 -*-

# 5.1 for

# for <statement>:
#     <processamento>

# 5.1.1 Escreva todos os números de 0-100


def get_num_until_100():
    """Método utilizado para ler todos os números de 0-100"""
    for i in range(101):
        print(i)


# get_num_until_100()

# 5.1.2 Escreva todos os números pares de 0-100


def get_even_num():
    """Metodo utilizado para retornar todos os números pares entre 0-100"""
    # for i in range(101):
    #     if i % 2 == 0:
    #         print(i)
    for i in range(0, 100, 2):
        print(i)


# get_even_num()

# 5.1.3 Escreva um programa que peça ao unuário um texto e depois imprima cada letra deste texto no console


def print_letter():
    "Metodo utilizado para imprimir todas as letras de um texto passado pelo usuário no console"
    texto = input("Digite um texto: ")

    for l in texto:
        print(l)


# print_letter()

# 5.1.4  Escreva um programa que peça ao unuário um texto e depois imprima o número de vogais deste texto no console


def print_vowels():
    """Método utilizado para imprimir vogais de um texto passado pelo usuáriio"""

    texto = input("Digite um texto: ")

    vogais = "aeiou"

    for i in texto:
        if i in vogais:
            print(i)


# print_vowels()

# 5.1.5 Escreva um programa que imprima as tres primeiras letras de cada palavra e a última vogal de cada palavra


def print_letters_and_last_vowal():
    "Método utilizado para imprimir as tres primeiras letras de cada palavra e a última vogal de cada palavra" ""

    text = input("Digite o um texto separado por espaços: ")

    vogais = "aeiou"

    # count_pos = 0
    ultima_vogal = ''

    # for l in text:
    #     if l != " ":
    #         if (count_pos < 3):
    #             count_pos += 1
    #             print("posição da letra {}: {}".format(l, count_pos))
    #         if l in vogais:
    #             ultima_vogal = l
    #     else:
    #         print("ultima vogal: {}".format(ultima_vogal))
    #         print("---------------")
    #         count_pos = 0
    #         ultima_vogal = ''

    # print("ultima vogal: {}".format(ultima_vogal))

    for palavra in text.split(" "):
        for i, l in enumerate(palavra, start=1):
            if i <= 3:
                print("posição da letra {}: {}".format(l, i))
            if l in vogais:
                ultima_vogal = l
            if i == len(palavra):
                print("ultima vogal: {}".format(ultima_vogal))

        print("---------------")


print_letters_and_last_vowal()

# 5.2 while
