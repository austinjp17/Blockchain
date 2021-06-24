import hashlib
import json
from time import time

class Blockchain(object):
    def __init__(self):
        self.chain = []     #BlockChain 
        self.pending = []   #Data waiting to be approved
        self.new_block(previous_hash = 'first', proof=100)    #Add block function
    
    def new_block(self, proof, previous_hash = None):
        block = {
            'index' : len(self.chain)+1,
            'timestamp' : time(),
            'data' : self.pending,
            'proof' : proof,
            'previous_hash' : previous_hash or self.hash(self.chain[-1])
        } 
           
        self.pending = []
        self.chain.append(block)
        return block
    @property
    def last_block(self):
        return self.chain[-1]
    def new_transactions(self, sender_address, receiver_address, data):

        transaction = {
            'sender' : sender_address,
            'reciever' : receiver_address,
            'data' : data
        }
        self.pending.append(transaction)
        return self.last_block['index'] + 1
    def hash(self, block):
        string_object = json.dumps(block, sort_keys=True)
        block_string = string_object.encode()
        raw_hash = hashlib.sha256(block_string)
        hex_hash = raw_hash.hexdigest()
        return hex_hash
    
if __name__ == "__main__":
    Blockchain().new_transactions('Austin', 'Antonio', '10 BTC')
    print(Blockchain().chain)
