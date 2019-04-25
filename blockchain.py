#!/usr/bin/env python3

import datetime
import hashlib


class Block:
    block_number = 0
    data = None
    next_block = None
    current_hash = None
    nonce = 0
    previous_hash = 0x0
    timestamp = datetime.datetime.now()

    def __init__(self, data):
        self.data = data

    def hash(self):
        h = hashlib.sha256()
        h.update(
            str(self.nonce).encode('utf-8') + 
            str(self.data).encode('utf-8') + 
            str(self.previous_hash).encode('utf-8') +
            str(self.timestamp).encode('utf-8') + 
            str(self.block_number).encode('utf-8')
        ) 
        return h.hexdigest()

    def __str__(self):
        return "Hash: " + str(self.hash()) + \
            "\n#: " + str(self.block_number) + \
            "\nData: " + str(self.data) + \
            "\nHashes: " + str(self.nonce) + \
            "\n-----"

class Blockchain:
    max_nonce = 2**32
    diff = 10
    target = 2**(256-diff)

    block = Block("Genesis")
    head = block
    
    def add(self, block):
        block.previous_hash = self.block.hash()
        block.block_number = self.block.block_number + 1

        self.block.next_block = block
        self.block = self.block.next_block

    def mine(self, block):
        for n in range(self.max_nonce):
            if int(block.hash(), 16) <= self.target:
                self.add(block)
                print(block)
                break
            else:
                block.nonce += 1

blockchain = Blockchain()
for n in range(10):
    blockchain.mine(Block("Block " + str(n + 1)))

while blockchain.head != None:
    print(blockchain.head)
    blockchain.head = blockchain.head.next_block

