# -*- coding: utf-8 -*-

# 4. Condicionais

# SE <condição> for verdadeira
#    faça alguma coisa
# ENTÃO
#     faça outra coisa

# SE -> if
# ENTÃO -> else

# 4.1 Revisão de operadores

# 4.2 Checar se um número é impar, par ou zero


def check_number() -> (bool, int):
    """Metodo utilizado para checar se um número dadoo pelo usuário é par ou impar

    return: Se é um número
    return: O número inseriddo
    """
    num = input("Digite um número inteiro: ")

    num = num.strip()

    if num.isdigit():
        num = int(num)
    else:
        print("Você não digitou um número inteiro")
        return False, num

    if num == 0:
        print("Este número é zero")
    elif num % 2 == 0:
        print("Este número é par")
    else:
        print("este número é impar")

    return True, num


# is_num, num = check_number()
# print("resposta para {}: {}".format(num, is_num))

# 4.3 Adivinhe meu número


def adivinhe_o_numero(num: int) -> None:
    """Metodo utilizado para adivinhhar um número pré-definido a partir do console

    param num: Número a ser adivinhado
    type num: int

    return: None
    """

    e_num, chute = check_number()

    if e_num:
        if chute == num:
            print("Parabéns! Você acertou")
        elif chute > num:
            print("Chutou muito alto")
        else:
            print("Chutou muito baixo!")


# adivinhe_o_numero(15)

# 4.4 Dada uma entrada do usuário, cheque se esse número é de telemarkt que possui 4 dígitos, o primeiro é 9 e o segundo e terceiro dígitos são iguais


def e_num_telemarkt() -> bool:
    """Método utilizado para checar se um número é de telemarkt da seguinte forma:
    - Tem 4 digitos
    - primeiro dígito é 9
    - segundo e terceiro digitos são iguais

    return: Verdadeiro ou falso
    """

    e_num, num = check_number()

    if e_num:
        num = str(num)
        if (len(num) != 4) or (num[0] != '9') or (num[1] != num[2]):
            print("Este não é um número de telemarkt")
            # print("Este número tem mais de 4 dígitos")
            return False
        # if num[0] != '9':
        #     print("Este número não começa com 9")
        #     return False
        # if num[1] != num[2]:
        #     print("O segundo e o terceeiro número são diferentes")
        #     return False

        print("Este é um número de telemarkt")
        return True


e_num_telemarkt()