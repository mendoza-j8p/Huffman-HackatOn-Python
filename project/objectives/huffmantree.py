from collections import Counter
from project.objectives.priorityqueue import PriorityQueue
from project.common.node import Node

class HuffmanTree:
    def __init__(self):
        self.root = None # Root node
        self.priority_queue = PriorityQueue(compare=lambda x : x[1]) # Priority Queue

    def create_huffman_tree(self,data):
        """
            Generates the whole HuffmanTree for a text passed as argument.
        """
        if not data:
            raise ValueError("Data cannot be empty")

        freq_dict = self.frequencies(data)

        for char, freq in freq_dict.items():
            node = self.create_node(char, freq)
            self.priority_queue.push((node, freq))

        while self.priority_queue.length() > 1:
            left = self.priority_queue.pop()
            right = self.priority_queue.pop()
            composed_node = self.compose_node(left[0], right[0])
            self.priority_queue.push((composed_node, composed_node.freq))
        self.root = self.priority_queue.pop()[0]

    def compose_node(self, left, right):
        """
            Creates a new Node without any character associated
        """
        if left is None or right is None:
            raise ValueError("Both left and right nodes must be provided")

        return self.create_node(None, left.freq + right.freq, left, right)

    def create_node(self, char, freq, left=None, right=None):
        return Node(char, freq, left, right)

    def frequencies(self, data):
        return dict(Counter(data))

    def get_codes(self):
        return self.get_codes_recursive(self.root, '')

    def get_codes_recursive(self, node, code):
        if node is None:
            return {}
        codes = {}

        if node.char is not None:
            codes[node.char] = code
        
        codes.update(self.get_codes_recursive(node.left, code + '0'))
        codes.update(self.get_codes_recursive(node.right, code + '1'))

        return codes

    def print_tree(self):
        self.print_tree_recursive(self.root, '')

    def print_tree_recursive(self, node, code):
        if node.char is not None:
            print("{} -> {}".format(node.char, code))

        if node.left is not None:
            self.print_tree_recursive(node.left, code + '0')
        if node.right is not None:
            self.print_tree_recursive(node.right, code + '1')
