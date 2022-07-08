from Content.Util import Util

from Model.Enum.TipoMovimentoEnum import TipoMovimentoEnum
from Model.UsuarioModel import UsuarioModel

from Controller.ConnectionDBController import ConnectionDBController

class AtmController:
    def __init__(self) -> None:
        self.conn = ConnectionDBController.get_connection()

    def menu_principal(self):
        print('=' * 30)
        print(f'{"Konv Mini Bank":^30}')
        while True:
            print('=' * 30)
            resposta = Util.criar_menu(['Entrar', 'Criar cadastro', 'Sair do sistema'])
            if resposta == 1:
                cpf = input('Digite seu cpf: ')
                cpf_validado = Util.validar_cpf(cpf)
                if cpf_validado:
                    usuario = UsuarioModel().logar(cpf, self.conn)
                    if usuario is not None:
                        while True:
                            print('=' * 30)
                            print(f'Usuário: {usuario.Nome}'.center(30))
                            print('-' * 30)
                            resposta = Util.criar_menu(['Depositar', 'Sacar', 'Extrato', 'Sair'])
                            if resposta == 1:
                                valor = Util.ler_inteiro("Digite o valor: ")
                                if valor <= 0:
                                    print("\033[91mValor insuficiente para deposito!\033[0m")
                                else:
                                    usuario.depositar(valor, self.conn)
                            elif resposta == 2:
                                valor = Util.ler_inteiro("Digite o valor: ")
                                if valor <= 0:
                                    print("\033[91mImpossível realizar saque com esse valor!\033[0m")
                                else:
                                    usuario.sacar(valor, self.conn, AtmController.verificar_cedulas)
                            elif resposta == 3:
                                extrato = usuario.obter_extrato(self.conn)
                                print('-' * 50)
                                print(f'{"Extrato":^50}')
                                print('-' * 50)
                                print("TIPO MOVIMENTAÇÃO | VALOR | DATA/HORA")
                                for item in extrato:
                                    if item.TipoMovimento == TipoMovimentoEnum.DEPOSITO.value:
                                        item.TipoMovimento = 'Depósito'
                                        separador = " " * 5
                                        separador_esq = " " * 3
                                    elif item.TipoMovimento == TipoMovimentoEnum.SAQUE.value:
                                        item.TipoMovimento = 'Saque'
                                        separador = " " * 6
                                        separador_esq = " " * 6

                                    print(f'{separador}{item.TipoMovimento}{separador_esq}    {Util.mascara_moeda(item.Valor)}   {item.DhMovimento.strftime("%d/%m/%Y %H:%M:%S")}')
                                print('-' * 50)
                                print(f'Saldo atual: R${Util.mascara_moeda(usuario.verificar_saldo)}'.center(50))
                                print('-' * 50)
                            elif resposta == 4:
                                print("Saindo da conta...")
                                break
                            else:
                                print("\033[91mOpção inválida!\033[0m")
                    else:
                        print("\033[91mUsuário não existe!\033[0m")
                else:
                    print('\033[91mCPF inválido!\033[0m')
            elif resposta == 2:
                nome = input("Digite seu nome: ")
                cpf = Util.validar_cpf(input("Digite seu cpf: "))
                if cpf:
                    cpf_ja_existe = UsuarioModel.cpf_existe(cpf, self.conn)
                    if cpf_ja_existe:
                        print('\033[91mCPF já cadastrado no sistema\033[0m')
                    else:
                        UsuarioModel.cadastrar(nome, cpf, self.conn)
                else:
                    print('\033[91mCPF inválido!\033[0m')
            elif resposta == 3:
                print("Saindo do sistema...")
                break
            else:
                print("\033[91mOpção inválida\033[0m")

    @staticmethod
    def verificar_cedulas(valor):
        ced = 100
        totced = 0
        while True:
            if valor >= ced:
                valor -= ced
                totced += 1
            else:
                if totced > 0:
                    print(f'Total de {totced} cédulas de R$ {ced}')
                if ced == 100:
                    ced = 50
                elif ced == 50:
                    ced = 20
                elif ced == 20:
                    ced = 10
                elif ced == 10:
                    ced = 5
                elif ced == 5:
                    ced = 2
                elif ced == 2:
                    ced = 1
                totced = 0
                if valor == 0:
                    break
