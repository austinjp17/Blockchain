from hashlib import sha256
import json
from time import time
from random import randint
from time import sleep

class Blockchain:
    
    def __init__(self):
        self.chain = []     #BlockChain 
        self.pending = []   #Data waiting to be approved    
        self.usedNonces = set()    
        self.gensis_block()    #Genesis Block
    
    def gensis_block(self, guess):
        genesis_block = {
            'index': 1,
            'nonce': guess,
            'Timestamp': time(),
            'initial': "Genesis Block",
            'previous_hash': "00"
        }
        self.chain.append(genesis_block)
        return genesis_block
        
    def new_block(self, guess = self.proof_of_work() , previous_hash=None, transactions = 'First', ):
        block = {
            'index': len(self.chain)+1,
            'nonce': guess,
            'Timestamp': time(),
            'transactions': transactions or self.pending,
            'previous_hash': previous_hash
        }
        
        if self.validation(block) is True:
            self.chain.append(block)
        with open('Output.txt', "w") as outputFile:
            print(str(self.chain).replace("'", "").replace("{", "").replace("}","")[1:-1], file=outputFile)
        return block
    
    def proof_of_work(self, block):
        nonce = 0
        #print(self.validation(self.new_block(guess=nonce)))
        while self.validation(self.new_block(guess=nonce)) is False:
            nonce +=1
        return nonce
    
    #@staticmethod
    def validation(self, block):
        hex_guess = self.hash(block)
        if hex_guess[:2] == '00':
            print(f'winner: {hex_guess}')
            return True
        return False
    
    def genesis_validation(self, block):
        nonce = 0
        hex_guess = self.hash(self.gensis_block(nonce))
        while hex_guess[:2] != '00':
            nonce +=1
            hex_guess = self.hash(self.gensis_block(nonce))
        print(f"winner for genesis: {nonce}")
        return nonce


    def nonceGuess(self):
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
        return int(self.last_block['index']) + 1
        
    @property
    def last_block(self):
        try:
            return self.chain[-1]
        except:
            pass

    @staticmethod 
    def hash(block):
        return sha256(json.dumps(block).encode('utf-8')).hexdigest()
    
if __name__ == "__main__":
    print(Blockchain().chain)
    #Blockchain().newTransaction(sender='Austin', reciever='Antonio', amount='Genisis Block')
    #with open('Output.txt', 'r') as f:

#74234e98afe7498fb5daf1f36ac2d78acc339464f950703b8c019892f982b90b