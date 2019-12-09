
from .common import common

class login(common):
    def __init__(self,pd):

        super(login, self).__init__(pd)
        self.post = pd
        
    
    def auth(self):

        try:
            sql = "SELECT * FROM auth_fn('{0}','')".format(
                    self.post['studentno'])

            print(sql)
            recs = self.conn.read(sql)
            
            return recs
        except Exception as ex:
            print(ex)
            return None
    
    def staff(self):
        try:
            sql = "SELECT * FROM staff_auth_fn('{0}','{1}')".format(self.post['unm'],self.post['pwd'])
            print(sql)
            recs = self.conn.read(sql)

            return recs
        except Exception as ex:
            print(ex)
            return None
    

    def search(self):
        try:
            sql = "SELECT * FROM find_fn('{0}')".format(self.post['studentno'])
            print(sql)
            recs = self.conn.read(sql)

            return recs
        except Exception as ex:
            print(ex)
            return None