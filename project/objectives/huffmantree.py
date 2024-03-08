from project.objectives.priorityqueue import PriorityQueue
from project.common.node import Node

class HuffmanTree:
    def __init__(self):
        self.root = None # Root node
        self.pq = PriorityQueue(compare=lambda x : x[1]) # Priority Queue

    def createHuffmanTree(self,data):
        """
            Generates the whole HuffmanTree for a text passed as argument. This method populates the HuffmanTree.
            @params data: Text to create the HuffmanTree.
            @returns: (void). It doesn't return anything.
        """
        pass

    def composeNode(self, left, right):
        """
            Creates a new Node without any character associated
            based on two nodes.
            @params: left node
            @params: right node

            @returns: A Node() composed from the left and right node but without any character associated.
        """
        if left is None or right is None:
            raise Exception
        
        return None

    def createNode(self, char, freq, left, right):
        """
            Instantiates and returns a new Node with params as
            its attributes.
            @param char: The character of the Node.
            @param freq: The frequency of the Node.
            @param left: The left child of the Node.
            @param right: The rigth child of the Node.
            @returns: A new Node() with params as attributes.
        """
        return None

    def frequencies(self, data):
        """
            Returns a dictionary with the frequencies of each character
            @params data: Plain text
            @returns: Dictionary containing key as each character and its value the amount of times the character appears in data.
        """

        return {}


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
