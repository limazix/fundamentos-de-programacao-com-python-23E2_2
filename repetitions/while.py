# -*- coding: utf-8 -*-

# 5. Repetições

# 5.2 while -> enquanto

# while <condição>:
#    <executar>

# 5.2.1 Escreva todos os números de 0-100


def get_num_until_100():
    """Método utilizado para ler todos os números de 0-100"""

    i = 0
    while i <= 100:
        print(i)
        i += 1


# get_num_until_100()

# 5.1.2 Escreva todos os números pares de 0-100


def get_even_num():
    """Metodo utilizado para retornar todos os números pares entre 0-100"""

    i = 0
    while i <= 100:
        print(i)
        i += 2


# get_even_num()

# 5.1.3 Escreva um programa que peça ao unuário um texto e depois imprima cada letra deste texto no console


def print_letter():
    "Metodo utilizado para imprimir todas as letras de um texto passado pelo usuário no console"
    texto = input("Digite um texto: ")

    pos = 0

    while pos < len(texto):
        print(texto[pos])
        pos += 1


# print_letter()

# um programa que peça ao unuário um texto e depois imprima o número de vogais deste texto no console


def print_vowels():

    texto = input("Digite um texto: ")

    vogais = "aeiou"

    pos = 0

    while pos < len(texto):
        c = texto[pos]
        if c in vogais:
            print(c)
        pos += 1


# print_vowels()

# 5.1.5 Escreva um programa que imprima as tres primeiras letras de cada palavra e a última vogal de cada palavra


def print_letters_and_last_vowal():
    "Método utilizado para imprimir as tres primeiras letras de cada palavra e a última vogal de cada palavra" ""

    text = input("Digite o um texto separado por espaços: ")

    vogais = "aeiou"

    pos = 0
    # count_pos = 0
    ultima_vogal = ''

    # while pos < len(text):
    #     l = textp" ":
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
    #     pos += 1

    # print("ultima vogal: {}".format(ultima_vogal))

    palavras = text.split(" ")

    while pos < len(palavras):
        palavra = palavras[pos]

        pos_palavra = 0

        while pos_palavra < len(palavra):
            l = palavra[pos_palavra]
            if pos_palavra < 3:
                print("posição da letra {}: {}".format(l, pos_palavra + 1))
            if l in vogais:
                ultima_vogal = l
            pos_palavra += 1
        print("ultima vogal: {}".format(ultima_vogal))
        pos += 1
        print("---------------")


print_letters_and_last_vowal()
