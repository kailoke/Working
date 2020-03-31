import pymysql as sql


class DBUtil:
    @classmethod
    def get_connection(cls, table_name):
        conn = sql.connect()


    @classmethod
    def intialize_table(cls, conn, table_name):
        print("ok")