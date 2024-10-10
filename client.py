class Blockchain(object):
    def __init__(self):
        self.chain = []
        self.current_transaction = []

    def new_block(self):
        #should create a new block and add it to chain
        return
    def helloworld(self):
        print("Hello World")
    
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
        #hashing
        return

    @property
    def last_block(self):
        #returns the last block in the chain
        return

Blockchain().helloworld()