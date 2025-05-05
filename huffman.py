# Brian Ochoa (beo3), Giovani Bergamasco (glb7), Victor Sima (vs77)
import heapq
class HuffmanNode:
    def __init__(self, char, freq, left=None, right=None):
        self.char = char
        self.freq = freq
        self.left = left
        self.right = right
    
    def __lt__(self, other):
        return self.freq < other.freq

#Created this class as a version of the huffman tree, where we do not know any frequencies.
#Therefore since we don't know any data it is 'unknown'.

class unknownHuffmanNode:
    def __init__(self):
        self.char = None
        self.left = None
        self.right = None

# Part a
def frequency_table(st: str) -> None:
    """
    Constructs a frequency table for each character in the string st and prints it.

    Parameters:
        st (str): A string with a maximum length of 256 characters.

    Output:
        Print each character along with its corresponding frequency.
    """

    #For this problem we literally cannot do anything that isn't O(n)
    #The problem does not assume that it contains numeric or any other characters.
    #For the beginning implementation, let's assume it's just lowercase letters.

    #Implemented Gio's version of the table below:

    #This simply creates the table
    frequency_table: dict[str, int] = {}

    # Loop through all characters in given string to fill the frequency table.
    # If a character already exists in the table increment the count, else make a new entry for it starting at 1.
    for char in st:
        if char in frequency_table:
            frequency_table[char] += 1
        else:
            frequency_table[char] = 1

    # Print the characters from the frequency table in sorted order (based on char).
    # repr() function allows for special characters like space to be represented.
    print("Character Frequencies:")
    for char in sorted(frequency_table):
        print(f"{repr(char)}: {frequency_table[char]}")


# Part b
def Huffman_code(st: str):
    """
    Builds a Huffman tree from the string st and generates the Huffman codes for each character. Print each character with its corresponding code.

    Parameters:
        st (str): A string with a maximum length of 256 characters.
    
    Output:
        Print the Huffman code for each character in the string. 
    """

    frequency_table: dict[str, int] = {}
    
    for char in st:
        if char in frequency_table:
            frequency_table[char] += 1
        else:
            frequency_table[char] = 1


    nTree_nodes = []

    for char, freq in frequency_table.items():
        heapq.heappush(nTree_nodes, HuffmanNode(char, freq))

    while len(nTree_nodes) > 1:

        left_subtree = heapq.heappop(nTree_nodes)
        right_subtree = heapq.heappop(nTree_nodes)

        merged_freq = left_subtree.freq + right_subtree.freq

        if (left_subtree.char is not None) and (right_subtree.char is not None):
            heapq.heappush(nTree_nodes, HuffmanNode(None, merged_freq, left_subtree, right_subtree))
        else:
            heapq.heappush(nTree_nodes, HuffmanNode(None, merged_freq, right_subtree, left_subtree))

    root = nTree_nodes.pop();
    huffman_code = tree_traversal(root, "", {}, None)
    print(huffman_code)
    return huffman_code

def tree_traversal(root:HuffmanNode, encoding: str, e_table: dict, parent: tuple):
    if root is None:
        return e_table

    if root.char is not None:
        e_table[root.char] = encoding
        return e_table

    tree_traversal(root.left, encoding+"0", e_table, parent)
    tree_traversal(root.right, encoding+"1", e_table, parent)

    return e_table

   

# Part c
def Huffman_encode(st: str, codes: dict):
    """
    Prints the binary encoded version of st, based on the Huffman codes generated in part (b) codes.

    Parameters:
        st (str): A string with a maximum length of 256 characters.
        codes: Huffman codes codes.

    Output:
        Print the binary-encoded string using the Huffman codes. 
    """
    encode = ""
    for char in st:
        encode += codes[char]
    print("Encoded String: "+encode+"\n")
    return encode


# Part d
def Huffman_tree(L: list):
    """
    Given a list L of characters and their corresponding Huffman codes; construct a Huffman tree based on this list.

    Parameters:
        L (list): A list L of characters and their corresponding Huffman codes.

    Output:
        Return the Huffman tree constructed from the list. 
    """

    root = unknownHuffmanNode()

    for char, code in L:
        node = root
        for path in code:
            if path == '0':
                if not node.left:
                    node.left = unknownHuffmanNode()
                node = node.left
            else:
                if not node.right:
                    node.right = unknownHuffmanNode()
                node = node.right
        node.char = char 
    
    return root


# Part e
def Huffman_decode(bst: str, tree: unknownHuffmanNode) -> None:
    """
    Decodes the binary-encoded text bst back into its original string using the Huffman tree.

    Parameters:
        bst (str): A binary-encoded string.
        tree (object): Huffman tree used for decoding.

    Output:
        Prints the decoded string.
    """
    decoded_string = ""

    root = tree
    node = root

    for bit in bst:
        if bit == '0':
            node = node.left
        else:
            node = node.right
        
        if not node.left and not node.right:
            decoded_string += node.char
            node = root
    
    print(decoded_string)
    

def main():
    st = "abbcccdddd" #example from assignment
    test_str = "a fast runner need never be afraid of the dark" #slide examples
    test_str2 = "Time to party like it's 2033." #Johnny Silverhand's famous slogan
    part1 = "I'd like to share a revelation that I've had during my time here."
    part2 = "It came to me when I tried to classify your species and I realized that you're not actually mammals. " 
    part3 = "Every mammal on this planet instinctively develops a natural equilibrium with the surrounding environment but you humans do not."
    test_str3 = part1 + part2 + part3 #Kudos if you know this one.


    frequency_table(st)
    frequency_table(test_str)
    frequency_table(test_str2)
    frequency_table(test_str3)
    codes = {"a": "000", "b": "001", "c": "01", "d": "1"}

    Huffman_code(st)
    test1 = Huffman_code(test_str)
    test2 = Huffman_code(test_str2)
    test3 = Huffman_code(test_str3)

    huffmanTest1 = list(test1.items())
    huffmanTest2 = list(test2.items())
    huffmanTest3 = list(test3.items())

    Huffman_encode(st, codes)
    Huffman_encode(test_str, test1)
    Huffman_encode(test_str2, test2)
    bst = Huffman_encode(test_str3, test3)

    L = [('a', '000'), ('b', '001'), ('c', '01'), ('d', '1')]
    L2 = huffmanTest1
    L3 = huffmanTest2
    L4 = huffmanTest3


    tree = Huffman_tree(L)
    tree2 = Huffman_tree(L2)
    tree3 = Huffman_tree(L3)
    tree4 = Huffman_tree(L4)

    Huffman_decode(bst, tree4)

if __name__ == "__main__":
    main()