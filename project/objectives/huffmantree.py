from collections import Counter
from project.objectives.priorityqueue import PriorityQueue
from project.common.node import Node

class HuffmanTree:
    def __init__(self):
        self.root = None # Root node
        self.pq = PriorityQueue(compare=lambda x : x[1]) # Priority Queue

    def createHuffmanTree(self,data):
        """
            Generates the whole HuffmanTree for a text passed as argument.
        """
        if not data:
            raise ValueError("Data cannot be empty")

        freq_dict = self.frequencies(data)

        for char, freq in freq_dict.items():
            node = self.createNode(char, freq)
            self.pq.push((node, freq))
        
        while self.pq.length() > 1:
            left = self.pq.pop()
            right = self.pq.pop() 
            composed_node = self.composeNode(left[0], right[0])
            self.pq.push((composed_node, composed_node.freq))
        self.root = self.pq.pop()[0]

    def composeNode(self, left, right):
        """
            Creates a new Node without any character associated
        """
        if left is None or right is None:
            raise ValueError("Both left and right nodes must be provided")
        
        return self.createNode(None, left.freq + right.freq, left, right)

    def createNode(self, char, freq, left=None, right=None):
        return Node(char, freq, left, right)

    def frequencies(self, data):
        return dict(Counter(data))


    def getCodes(self):
        return self.getCodesRecursive(self.root, '')

    def getCodesRecursive(self, node, code):
        return {}

    def printTree(self):
        self.printTreeRecursive(self.root, '')
        
    def printTreeRecursive(self, node, code):
        if node.char is not None:
            print("{} -> {}".format(node.char, code))

        if node.left is not None:
            self.printTreeRecursive(node.left, code + '0')
        if node.right is not None:
            self.printTreeRecursive(node.right, code + '1')
