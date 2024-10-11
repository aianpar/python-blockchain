import hashlib
import json
from time import time

class Blockchain(object):
    def __init__(self):
        self.chain = []
        self.current_transaction = []

        # Create the genesis block
        self.new_block(previous_hash=1, proof=100)

    def new_block(self,proof,previous_hash=None):
        #should create a new block and add it to chain
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions': self.current_transaction,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1]),
        }

        self.current_transaction = []
        self.chain.append(block)
        return block
        
    def helloworld(self):
        print("Hello World")
        print(hashlib.sha256("Hello World".encode()).hexdigest())
        return
    
    def new_transaction(self,sender,recipient,amount):
        """
        sender:<str>
        recipient: <str>
        amount: <int>
        return: <int>
        """
        self.current_transaction.append({
            'sender':sender,
            'recipient':recipient,
            'amount': amount,
        })
        return self.last_block['index']+1
    
    
    @staticmethod
    def hash(block):
        """
        :param block: <dict> Block
        :return: <str> Hash256 of block
        """
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    @property
    def last_block(self):
        #returns the last block in the chain
        return self.chain[-1]

Blockchain().helloworld()