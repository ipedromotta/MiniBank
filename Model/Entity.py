class Entity(list):

    @staticmethod
    def __loadAll__(conn, query):
        try:
            cursor = conn.cursor(dictionary=True)
            cursor.execute(query)
            rows = cursor.fetchall()
            cursor.close()

            return rows
        except Exception as ex:
            return list()

    @staticmethod
    def __load__(conn, query):
        try:
            cursor = conn.cursor(dictionary=True)
            cursor.execute(query)
            rows = cursor.fetchone()
            cursor.close()

            return rows
        except Exception as ex:
            return list()

    @staticmethod
    def __toList__(t, rows):
        _list = list()

        try:
            for row in rows:
                try:
                    obj = t(**row)
                    _list.append(obj)
                except Exception as ex:
                    pass 

            return _list
        except Exception as ex:
            _list = list()

        return _list

    @staticmethod
    def __toObject__(t, rows):
        _obj = None

        try:
            for row in rows:
                _obj = t(**row)
                break
        except Exception as ex:
            _obj = None

        return _obj

    @staticmethod
    def Execute(query, conn):
        try:
            cursor = conn.cursor()
            cursor.execute(query)
            conn.commit()
            cursor.close()
        except Exception as ex:
            pass
