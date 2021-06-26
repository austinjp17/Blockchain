import hashlib
from random import randint

class test:

    def hash(self):
        i = 3
        self.previous_hash = '74703b00d6f13885bef79a04ee1eaf4abfd9ae237afc719fd28f90ee6287da0d'
        myblock = {
            'index': i,
            'data': 'austin',
            'nonce': randint(0,100),
            'prev_hash': self.previous_hash
        }
        a = myblock.encode()
        
        hashlib.sha256(a).hexdigest()
    def proof_of_work(self):
        nonce = 1
        while self.validation(nonce, prev_hash) is False:
            nonce +=1
            print(nonce)
    def validation(self, nonce):

        return hexi_guess[:2] == "00"

if __name__ == "__main__":
    test().proof_of_work()