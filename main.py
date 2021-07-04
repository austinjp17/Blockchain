from hashlib import sha256
import json, time
from os import path
from random import randint, choice

class Blockchain:
    def __init__(self):
        self.difficulty = "000"
        self.num_blks_to_chk = 3
        self.chain = []     #BlockChain 
        self.pending = []   #Data waiting to be approved
        self.num_of_transactions_per = 10
        self.chain_file_path = "/Users/austin/Documents/GitHub/Blockchain/full_chain.json"  
        
    
    def genesis_block(self, guess):
        genesisBlock = {
            "index": 1,
            "nonce": guess,
            "Timestamp": time.time(),
            "initial": "Genesis Block",
            "previous_hash": "00"
        }
        if self.hash(genesisBlock)[:3] == self.difficulty: self.chain.append(genesisBlock)
        return genesisBlock
        
    def new_block(self, guess):
        block = {
            "index": len(self.chain)+1,
            "nonce": guess,
            "timestamp": time.time(),
            "transactions": self.pending,
            "previous_hash": self.hash(self.last_block)
        }
        if self.hash(block)[0:3] == self.difficulty: self.chain.append(block)
        return block
    
    def proof_of_work(self, block):
        nonce = 0
        #print(self.validation(self.new_block(guess=nonce)))
        while self.validation(self.new_block(guess=nonce)) is False:
            nonce +=1
        return nonce
    
    def validation(self):
        nonce = 0
        hex_guess = self.hash(self.new_block(nonce))
        while hex_guess[:3] != self.difficulty:                               #change difficulty in newblock & validation functions, bad
            nonce +=1
            hex_guess = self.hash(self.new_block(nonce))
            #print(f"\nhexidecimal: {hex_guess}\nnonce: {nonce} \n") #<- next hexidecimal & nonce attempt
            #time.sleep(1)
        self.successful_hash = hex_guess
        print(f"Nonce:{nonce}\nHexidecimal: {hex_guess}\n")       #Successful hexidecimal & nonce
        return nonce

    def genesis_validation(self):
        nonce = 0
        hex_guess = self.hash(self.genesis_block(nonce))
        while hex_guess[:3] != self.difficulty:
            nonce +=1
            hex_guess = self.hash(self.genesis_block(nonce))
        return nonce

    def newTransaction(self, *transactions):
        for sender, reciever, amount in transactions:
            self.pending.append({
                "transaction" : len(self.pending),
                "sender": sender,
                "reciever": reciever,
                "amount": amount,
            })
            if len(self.pending) >= self.num_of_transactions_per:
                print(f"{self.num_of_transactions_per} instances in pending list reached. Validating...")
                self.validation()
                self.pending = []
        
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
        return sha256(json.dumps(block).encode("utf-8")).hexdigest()
    @staticmethod
    def write_out(output, file_path):
        with open(file_path, "w") as outputFile:
            json.dump(output, outputFile)
    def pretty_write_out(self):
        with open(self.chain_file_path) as f:
                f = json.load(f)
                for k, v in f.items():
                    print(f"{k} : {v}") 
    def chain_verification(self, their_chain):
        with open(self.chain_file_path) as master:
            their_block_compare = None
            correct_block_compare = None
            correct_chain = json.loads(master.read())
            # print(str(len(their_chain)), str(len(correct_chain)))
            # print(len(correct_chain))
            random_index = randint(0,len(correct_chain))-1
            for i in range(0, len(correct_chain)-1):
                if int(correct_chain[i]['index']) == random_index:
                    correct_block_compare = correct_chain[i]['index']
            for i in range(0, len(correct_chain)-1):        
                if int(their_chain[i]['index']) == random_index:
                    their_block_compare = their_chain[i]['index']
            
            return(their_block_compare == correct_block_compare)

    def view_block(self, block_num, key=None):
        if key is None: return self.chain[block_num]
        else: return self.chain[block_num][key]
        
    def start_check_list(self, filepath=None):
        results = []
        if path.exists(self.chain_file_path or filepath) is True: #file exists
            print("Chain found, verifying..")
            with open(self.chain_file_path or filepath) as f:
                their_chain = json.loads(f.read())
                for i in range(self.num_blks_to_chk):
                    results.append(self.chain_verification(their_chain))
            if all(results) is True:
                #verified, break loop
                self.genesis_validation()
                
            
                

                #doesn't work, need to compare text. Maybe compare last few blocks, option?
        else: #doesn"t exist or incorrect path
            print(">> File not found. Change file path or wait for download to begin")
            time.sleep(1)
            print(">> Downloading Blockchain..")
            #download chain from somewhere
    
    def main(self):
        # for i in range(20):
        self.start_check_list()
        print('Verified')
        #self.write_out(output=None)        
        #for i in range(20, randint(100,500)):
        for i in range(55):
            with open("first-names.txt", "r") as file:
                name = choice(list(file))                
                amount = randint(1,3000)
                self.newTransaction((name[:3], name[2:],str(amount)+" BTC"))
        self.write_out(self.chain, file_path=self.chain_file_path)
        return(len(self.pending), self.view_block(block_num=-1)['index'], self.view_block(-1))

            #self.newTransaction(())
        #self.newTransaction(("Austin","Antonio","20 BTC"),("Vader","Frodo","8 BTC"),("Will","Sam","1000 BTC"),("Arron","Annie","1000 BTC"),("Ace","Ryan","103 BTC"),("Adam","Leslie","1090 BTC"),("Deandre","Houston","90 BTC"))
        #self.newTransaction(("After", "Write", "$1"))


    
if __name__ == "__main__":
    start_time = time.time()
    still_pending,num_of_blks, last_block = Blockchain().main()
    print()
    runtime = round(time.time() - start_time, 2)
    print(f'\nLast Block:\n{last_block}\n\nStill Pending: {still_pending}\nRuntime: {str(runtime)} seconds \nBlock created every {runtime/num_of_blks} seconds')
    # with open('/Users/austin/Documents/GitHub/Blockchain/full_chain.json', 'r') as full_block_list:
    #     print(full_block_list.read())

#number transactions
#Verification prob when difficulty changed
#compare block validation to other nodes
#chain is starting from scratch each time
#download chain if not found
#reward system?
#data being sent?