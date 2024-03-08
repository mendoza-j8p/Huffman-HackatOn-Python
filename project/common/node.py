class Node: 
    def __init__(self, char, freq, left=None, right=None):
        self.char = char
        self.freq = freq
        self.left = left
        self.right = right

    def __str__(self):
        return "Char: {} | Freq: {}".format(self.char, self.freq)
