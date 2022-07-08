import mysql.connector

from Model.Configuration import Configuration


class ConnectionDBController:

    @staticmethod
    def get_connection():
        try:
            (host, database, user, passwd) = Configuration().Database

            cnxn = mysql.connector.connect(
                host=host,
                user=user,
                passwd=passwd,
                database=database
            )
            return cnxn
        except Exception as ex:
            raise ex
