from .common import common

import config
import json
import requests
import random
import string

class payment(common):
    def __init__(self,pd):

        super(payment, self).__init__(pd)
        self.post = pd
        
    
    def randomReciept(self,studentno,length):

      reciept = ''.join(random.choice(string.digits) for i in range(length))

      return reciept + studentno[6:]


    def send(self):
        try:
          print(self.randomReciept(self.post['studentno'],7))
          transaction_id = self.randomReciept(self.post['studentno'],7)
          data = {
              "merchant_id":config.api_id,
              "transaction_id": transaction_id,
              "desc": "Payment for Graduation",
              "amount":"000000000100",
              "redirect_url": "http://kstugraduate.loc/fallback.php",
              "email": "mail@customer.com"
            }
          headers = {
              'Content-Type':'application/json',
              'Authorization': config.API_AUTH,
              'Cache-Control': 'no-cache'
          }
          # store receiptno
          
          
          req = requests.post(url=config.endpoint, data = json.dumps(data),headers=headers)

          print(json.loads(req.text))
          if json.loads(req.text)['status'] == 'success':
            print(json.loads(req.text))
            sql = "SELECT * FROM update_payment_fn('{0}','{1}','{2}')".format(
              self.post['studentno'],200,transaction_id)
            print(sql)
            recs = self.conn.read(sql)

            

          return json.loads(req.text)


        except Exception as ex:
            print(ex)
            return None

    def confirm(self):
      try:
        sql = "SELECT * FROM confirm_payment_fn('{0}','{1}')".format(
              self.post['studentno'],self.post['rcptno'])

        print(sql)
        recs = self.conn.read(sql)
        return recs
      except Exception as ex:
        print(ex)
        return None
      finally:
        print('hellooooooo')


    def attendance(self):
      try:
        sql = "SELECT * FROM confirm_attendance_fn('{0}')".format(self.post['studentno'])
        print(sql)
        recs = self.conn.read(sql)
        return recs
      except Exception as ex:
        print(ex)
        return None
      finally:
        print('hellooooooo')


    def bankpay(self):
      try:
        # Implement Bank pay here
        print(self.post)
      except Exception as ex:
        print(ex)
        return None
