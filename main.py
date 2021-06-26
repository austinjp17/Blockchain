from hashlib import sha256
import json, time
from random import randint
from typing import ChainMap

class Blockchain:
    
    def __init__(self):
        self.chain = []     #BlockChain 
        self.pending = []   #Data waiting to be approved    
        self.usedNonces = set()  
        
    
    def genesis_block(self, guess):
        genesisBlock = {
            'index': 1,
            'nonce': guess,
            'Timestamp': time.time(),
            'initial': "Genesis Block",
            'previous_hash': "00"
        }
        if self.hash(genesisBlock)[:2] == "00": self.chain.append(genesisBlock)
        return genesisBlock
        
    def new_block(self, guess):
        block = {
            'index': len(self.chain)+1,
            'nonce': guess,
            'Timestamp': time.time(),
            'transactions': self.pending,
            'previous_hash': self.hash(self.last_block)
        }
        if self.hash(block)[0:3] == "000": self.chain.append(block)
        return block
    
    def proof_of_work(self, block):
        nonce = 0
        #print(self.validation(self.new_block(guess=nonce)))
        while self.validation(self.new_block(guess=nonce)) is False:
            nonce +=1
        return nonce
    
    #@staticmethod
    def validation(self):
        nonce = 0
        hex_guess = self.hash(self.new_block(nonce))
        while hex_guess[:3] != '000':                               #Have to change difficulty in newblock & validation functions, bad
            nonce +=1
            hex_guess = self.hash(self.new_block(nonce))
        print(f"Success: {hex_guess[:5]}\nnonce:{nonce}")
        return nonce

    
    def genesis_validation(self):
        nonce = 0
        hex_guess = self.hash(self.genesis_block(nonce))
        while hex_guess[:2] != '00':
            nonce +=1
            hex_guess = self.hash(self.genesis_block(nonce))
        return nonce

    def newTransaction(self, *transactions):
        transactionCounter = 0  
        for sender, reciever, amount in transactions:
            self.pending.append({
                'transaction' : transactionCounter,
                'sender': sender,
                'reciever': reciever,
                'amount': amount,
            })
            transactionCounter+=1
            if len(self.pending) >= 2:
                self.validation()
                self.pending = []
                transactionCounter = 0
        
    def iterate_through_transactions(self):
        for item in self.pending:
            return(item)
        
    @property
    def last_block(self):
        try:
            return self.chain[-1]
        except:
            pass

    @staticmethod 
    def hash(block):
        return sha256(json.dumps(block).encode('utf-8')).hexdigest()
    
    def main(self):
        self.genesis_validation()
        self.newTransaction(('Austin','Antonio','20 BTC'),('Vader','Frodo','8 BTC'),('Will','Sam','1000 BTC'),('Will','Same','1000 BTC'),('Ace','Ryan','103 BTC'),('Adam','Leslie','1090 BTC'),('Deandre','Houston','90 BTC'))
        
        with open('full_chain.txt', "w") as outputFile:
            for block in self.chain:
                for key, value in block.items():
                    print(f"k: {key}\nv: {value}")
                print(f"{str(block)} \n".replace("'", "").replace("{", "").replace("}",""), file=outputFile)
        return(f"still pending: {self.pending}\nchain: {self.chain}")


    
if __name__ == "__main__":
    Blockchain().main()
    
    
    #with open('Output.txt', 'r') as f:

#difficulty function
#multithreading nonce attempts