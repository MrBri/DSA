import hashlib
import datetime
import unittest

class Block:
    def __init__(self, data, previous_block=None, timestamp=None):
        self.data = data
        self.previous_block = previous_block
        self.timestamp = timestamp or datetime.datetime.now()
        self.hash = self.calc_hash()

    def calc_hash(self):
        sha = hashlib.sha256()
        hash_str = str(self.timestamp) + str(self.data)
        if self.previous_block:
            hash_str += self.previous_block.hash
        sha.update(hash_str.encode('utf-8'))
        return sha.hexdigest()

class BlockChain:
    def __init__(self):
        self.head = None

    def append(self, data):
        if data is None:
            raise ValueError("Data cannot be None")
        elif not data:
            raise ValueError("Data cannot be empty")

        if not self.head:
            self.head = Block(data)
        else:
            node = Block(data, self.head)
            self.head = node

    def print_nodes(self):
        curr = self.head
        while curr:
            print(f"Timestamp: {curr.timestamp}, Data: {curr.data}, Hash: {curr.hash}")
            curr = curr.previous_block

chain = BlockChain()
chain.append("This is the first")
chain.append("Second in the chain")
chain.append("Third")
chain.print_nodes()

class TestBlockchain(unittest.TestCase):
    def test_add_block_with_none_data(self):
        blockchain = BlockChain()
        with self.assertRaises(ValueError) as context:
            blockchain.append(None)
        self.assertEqual(str(context.exception), "Data cannot be None")

    def test_add_block_with_empty_data(self):
        blockchain = BlockChain()
        with self.assertRaises(ValueError) as context:
            blockchain.append("")
        self.assertEqual(str(context.exception), "Data cannot be empty")

if __name__ == '__main__':
    unittest.main()

'''
def calc_hash(self):
      sha = hashlib.sha256()

      hash_str = "We are going to encode this string of data!".encode('utf-8')

      sha.update(hash_str)

      return sha.hexdigest()
'''
