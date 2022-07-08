from Model.Entity import Entity


class ExtratoModel(Entity):
    def __init__(self, ID=None, ID_USUARIO=None, DH_MOVIMENTO=None, TIPO_MOVIMENTO=None, VALOR=None):
        super(Entity, self)
        self.Id = ID
        self.IdUsuario = ID_USUARIO
        self.DhMovimento = DH_MOVIMENTO
        self.TipoMovimento = TIPO_MOVIMENTO
        self.Valor = VALOR

    def obter_extrato(self, id_usuario, conn):
        query = f'SELECT * FROM EXTRATO WHERE ID_USUARIO = {id_usuario}'

        rows = self.__loadAll__(conn, query)
        obj = self.__toList__(ExtratoModel, rows)

        return obj