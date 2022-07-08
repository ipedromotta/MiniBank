import re


class Util:
    def __init__(self):
        pass

    @staticmethod
    def mascara_moeda(valor):
        try:
            a = '{:,.2f}'.format(float(valor))
            b = a.replace(',','v')
            c = b.replace('.',',')
            return c.replace('v','.')
        except Exception as ex:
            pass

    @staticmethod
    def validar_cpf(cpf):
        cpf = ''.join(re.findall(r'\d', str(cpf)))

        if not cpf or len(cpf) < 11:
            return False

        antigo = [int(d) for d in cpf]

        novo = antigo[:9]
        while len(novo) < 11:
            resto = sum([v * (len(novo) + 1 - i) for i, v in enumerate(novo)]) % 11

            digito_verificador = 0 if resto <= 1 else 11 - resto

            novo.append(digito_verificador)

        if novo == antigo:
            return cpf

        return False

    @staticmethod
    def ler_inteiro(msg):
        while True:
            try:
                n = int(input(msg))
            except(ValueError, TypeError):
                print('\033[31mERRO: Por favor, digite um número inteiro válido.\033[m')
                continue
            except(KeyboardInterrupt):
                print('\n\033[31mUsuário preferiu não digitar esse número.\033[m')
                return 0
            else:
                return n
    
    @staticmethod
    def criar_menu(lista):
        contador = 1
        for item in lista:
            print(f'\033[33m{contador}\033[m - \033[34m{item}\033[m')
            contador += 1
        print('=' * 30)
        opc = Util.ler_inteiro('\033[32mSua Opção: \033[m')
        return opc
