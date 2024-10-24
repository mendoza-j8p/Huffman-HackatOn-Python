from project.objectives.huffmantree import HuffmanTree

class HuffmanCoding:
    """
        Encoding and decoding of data using Huffman Coding text compression
    """

    @staticmethod
    def encode(data):
        """
            Generates a HuffmanTree and creates an encoded data (in binary string) from the data parameter.
            @params: data is a string of characters.
            @returns: A tuple with the encoded data and the associated HuffmanTree.
        """

        if not data:
            return ("", None)  # Retorna None para el árbol si no hay datos

        # Crear el árbol de Huffman
        huffman_tree = HuffmanTree()
        huffman_tree.createHuffmanTree(data)

        # Obtener los códigos de Huffman
        huffman_codes = huffman_tree.getCodes()

        # Codificar los datos
        encoded_data = ''.join(huffman_codes[char] for char in data)

        return (encoded_data, huffman_tree)
    
    @staticmethod
    def decode(encodedData, huffmanTree=None):
        """
            Decodes into text the encodedData using the huffmantree passed as a parameter.
            @param encodedData: Binary string representation of encoded text. 
            @param huffmanTree: HuffmanTree object representation created from the decoded version of the encoded data. This will be used to decode the encodedData parameter.
            @returns: decoded data (plain text) using the huffmanTree and the encodedData parameters.
        """
        if huffmanTree is None:
            raise ValueError("HuffmanTree must be provided for decoding.")

        decoded_data = []
        current_node = huffmanTree.root

        for bit in encodedData:
            # Navegar el árbol de Huffman según el bit
            if bit == '0':
                current_node = current_node.left
            else:
                current_node = current_node.right

            # Si es una hoja, añadir el carácter al resultado
            if current_node.char is not None:
                decoded_data.append(current_node.char)
                current_node = huffmanTree.root  # Reiniciar al nodo raíz

        return ''.join(decoded_data)
