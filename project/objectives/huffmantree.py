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
        if not data:
            raise ValueError("Data cannot be empty")  # O cualquier otra validación que necesites
        
        # Paso 1: Obtener las frecuencias de los caracteres
        freq_dic = self.frequencies(data)

        # Paso 2: Crear nodos para cada carácter y añadirlos a la PriorityQueue
        for char, freq in freq_dic.items():
            node = self.createNode(char, freq) # Crea un nodo para cada carácter
            self.pq.push((node, freq)) # Añade el nodo a la PriorityQueue
        
        # Paso 3: Construir el árbol de Huffman
        while self.pq.length() > 1:
            left = self.pq.pop() # Saca el nodo con menor frecuencia
            right = self.pq.pop() # Saca el segundo nodo con menor frecuencia
            composed_node = self.composeNode(left[0], right[0]) # Crea un nodo compuesto a partir de los dos nodos sacados
            self.pq.push((composed_node, composed_node.freq)) # Añade el nodo compuesto a la PriorityQueue
        self.root = self.pq.pop()[0]  # Paso 4: Asignar la raíz del árbol de Huffman. Este será el nodo raíz

    def composeNode(self, left, right):
        """
            Creates a new Node without any character associated
            based on two nodes.
            @params: left node
            @params: right node

            @returns: A Node() composed from the left and right node but without any character associated.
        """
        if left is None or right is None:
            raise Exception("Both left and right nodes must be provided")
        
        return self.createNode(None, left.freq + right.freq, left, right)

    def createNode(self, char, freq, left=None, right=None):
        """
            Instantiates and returns a new Node with params as
            its attributes.
            @param char: The character of the Node.
            @param freq: The frequency of the Node.
            @param left: The left child of the Node.
            @param right: The rigth child of the Node.
            @returns: A new Node() with params as attributes.
        """
        return Node(char, freq, left, right)

    def frequencies(self, data):
        """
            Returns a dictionary with the frequencies of each character
            @params data: Plain text
            @returns: Dictionary containing key as each character and its value the amount of times the character appears in data.
        """
        freq_dic = {}

        for char in data:
            if char in freq_dic:
                freq_dic[char] += 1
            else:
                freq_dic[char] = 1


        return freq_dic


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
