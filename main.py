import sys
import re

from project.objectives.huffmantree import HuffmanTree
from project.objectives.huffmancoding import HuffmanCoding

data = "This is a test"
huffman = HuffmanTree()
huffman.create_huffman_tree(data)
codes = huffman.get_codes()

encodedText, huffmanTree = HuffmanCoding.encode(data)
decodedText = HuffmanCoding.decode(encodedText, huffmanTree)

print("Data is {}".format(data))
print("Encoded data is is {}".format(encodedText))
print("Decoded data is is {}".format(decodedText))


lenHuff = len(encodedText)
lenData = len(data) * 8

diff = lenData - lenHuff

print("Bits in huffman coding-> {}".format(len(encodedText)))
print("Bits in without huffman compression-> {}".format(len(data) * 8))
print("Difference {} - {} -> {}".format(lenData, lenHuff, diff))

