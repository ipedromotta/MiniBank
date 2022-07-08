from Model.Entity import Entity
from Model.ExtratoModel import ExtratoModel
from Model.Enum.TipoMovimentoEnum import TipoMovimentoEnum

class UsuarioModel(Entity):
    def __init__(self, ID=None, NOME=None, CPF=None, SALDO=None):
        super(Entity, self)
        self.Id = ID
        self.Nome = NOME
        self.Cpf = CPF
        self.__Saldo = SALDO

    def logar(self, cpf, conn):
        try:
            cursor = conn.cursor(dictionary=True)

            query = f"SELECT * FROM USUARIOS WHERE CPF = {cpf}"
            row = self.__load__(conn, query)
            cursor.close()

            obj = UsuarioModel(**row)
            obj.__Saldo = float(obj.__Saldo)
            return obj

        except Exception as ex:
            return None

    @property
    def verificar_saldo(self):
        return self.__Saldo

    def sacar(self, valor, conn, verificar_cedulas):
        if valor <= self.__Saldo:
            self.__Saldo -= valor
            self.__alterar_saldo(self.Id, valor, TipoMovimentoEnum.SAQUE.value, conn)
            verificar_cedulas(valor)
            print("Saque realizado com sucesso!")
        else:
            print("\033[91mSaldo insuficiente\033[0m")

    def depositar(self, valor, conn):
        self.__Saldo += valor
        self.__alterar_saldo(self.Id, valor, TipoMovimentoEnum.DEPOSITO.value, conn)
        print("Depósito realizado com sucesso!")

    def obter_extrato(self, conn):
        return ExtratoModel().obter_extrato(self.Id, conn)

    def __alterar_saldo(self, id_usuario, valor, tipo_movimento, conn):
        try:
            cursor = conn.cursor()
            query = "SP_ALTERAR_SALDO"
            cursor.callproc(query, (id_usuario, self.__Saldo, valor, tipo_movimento))
            conn.commit()
        except Exception as ex:
            pass

    @staticmethod
    def cadastrar(nome, cpf, conn):
        cursor = conn.cursor()
        query = "INSERT INTO USUARIOS (NOME, CPF) VALUES (%s, %s)"
        info = (nome, cpf)
        try:
            cursor.execute(query, info)
            conn.commit()
            print("Usuario cadastrado com sucesso!")
        except Exception as ex:
            print("Erro ao cadastrar usuario")

    @staticmethod
    def cpf_existe(cpf, conn):
        cursor = conn.cursor()
        query = f"SELECT * FROM USUARIOS WHERE CPF ='{cpf}'"
        cursor.execute(query)
        row = cursor.fetchone()
        if row:
            return True
            
        return False
