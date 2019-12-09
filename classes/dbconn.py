import psycopg2 as pg
import psycopg2.extras as pgextras
import config


class dbconn(object):
    def __init__(self, *kwargs):
        self.constr = config.DATABASE_STR
        self.conn = None

    def connect(self):
        try:
            self.conn = pg.connect(self.constr)
            return True
        except Exception as ex:
            print(ex)
            return self.conn
    

    def read(self,sql):
        rows = None
        try:
            self.connect()
            cur = self.conn.cursor(cursor_factory=pgextras.RealDictCursor)
            print(sql)
            cur.execute(sql)
            rows = cur.fetchall()

            self.conn.commit()

            return rows

        except Exception as ex:
            print(ex)
            return None

        finally:
            self.disconnect()


    def disconnect(self):
        if self.conn:
            self.conn.close()