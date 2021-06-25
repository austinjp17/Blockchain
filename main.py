import hashlib
import json
from time import time
from random import randint

class Blockchain:
    
    def __init__(self):
        self.chain = []     #BlockChain 
        self.pending = []   #Data waiting to be approved    
        self.usedNonces = set()    
        self.new_block(previous_hash = '00', transactions="Genesis Block")    #Genesis Block
    
    def new_block(self, transactions = None, previous_hash = None):

        block = {
            'index': len(self.chain)+1,
            'nonce': self.uniqueNonce(),
            'Timestamp': time(),
            'transactions': transactions or self.pending,
            'previous_hash': previous_hash or self.hash(self.chain[-1])
        }
        self.chain.append(block)
        with open('Output.txt', "w") as outputFile:
            print(str(self.chain).replace("'", "").replace("{", "").replace("}","")[1:-1], file=outputFile)
        return block
    
    def Validation(self, hash):
        nonce = 0
        while 
    def proof_of_work(self, nonce, previous_hash):
        pass()
    
    def uniqueNonce(self):
        nonce = randint(1,1000)
        if nonce in self.usedNonces: nonce = randint(1,1000)    #check if nonce used before
        self.usedNonces.add(nonce)
        return nonce

    def newTransaction(self, sender, reciever, amount):
        self.pending.append({
            'sender': sender,
            'reciever': reciever,
            'amount': amount,
        })
        self.new_block()
        return int(self.last_block['index']) + 1
        
    @property
    def last_block(self):
        return self.chain[-1]
    @staticmethod 
    def hash(block):
        blockAsString = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(blockAsString).hexdigest()
    
if __name__ == "__main__":
    Blockchain().newTransaction(sender='Austin', reciever='Antonio', amount='Genisis Block')
    #with open('Output.txt', 'r') as f:


#Save nonces to not be used again