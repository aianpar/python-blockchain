class Blockchain(object):
    def __init__(self):
        self.chain = []
        self.current_transaction = []

    def new_block(self):
        #should create a new block and add it to chain
    
    def new_transaction(self):
        #adds a new transaction to the list of current transactions
    
    @staticmethod
    def hash(block):
        #hashinh

    @property
    def last_block(self):
        #returns the last block in the chain
