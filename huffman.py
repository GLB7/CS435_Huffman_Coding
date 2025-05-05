# Brian Ochoa (beo3), Giovani Bergamasco (glb7), Victor Sima (vs77)

# Part a
def frequency_table(st: str) -> None:
    """
    Constructs a frequency table for each character in the string st and prints it.

    Parameters:
        st (str): A string with a maximum length of 256 characters.

    Output:
        Print each character along with its corresponding frequency.
    """
    # Example of this initalized table on Greedy Method 1 Slide 36
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
import heapq

class TreeNode:
    def __init__(self, val=0, left=None, right=None, c=''):
        self.val = val
        self.left = left
        self.right = right
        self.c = c
    
    # “<” so heapq can compare nodes (by frequency) when pushing/popping to heapify
    def __lt__(self, other):
        return self.val < other.val

def inorderTraversal(root, encoding, codes=None):
    if codes is None:
            codes = {}

    if(root==None):
        return 
    inorderTraversal(root.left, encoding+"0", codes)
    if root.c:
        print("\'" + root.c + "\' " , ":", encoding)
        codes[root.c] = encoding
    inorderTraversal(root.right, encoding+"1", codes)
    return codes

def Huffman_code(st: str):
    """
    Builds a Huffman tree from the string st and generates the Huffman codes for each character. Print each character with its corresponding code.

    Parameters:
        st (str): A string with a maximum length of 256 characters.
    
    Output:
        Print the Huffman code for each character in the string. 
    """
    if st == "":
        print("Huffman Codes:\nNone")
        return {}
    
    # Make Frequency Table of characters
    freq_table = {}

    # O(n) where n is length of string
    for c in st:
        if c not in freq_table:
            freq_table[c] = 1
        else:
            freq_table[c] +=1
    
    # Make a tree node for every character, we want a heap of tree nodes
    tree_nodes = []
    for key in freq_table:
        heapq.heappush(tree_nodes, TreeNode(freq_table[key], c=key))

    while len(tree_nodes)>1:
        c1 = heapq.heappop(tree_nodes)
        c2 = heapq.heappop(tree_nodes)
        
        # If c1 is new node, add it on the right
        if c1.c !='' and c2.c =='':
            heapq.heappush(tree_nodes, TreeNode(c1.val + c2.val, left=c2, right = c1))

        # Else, then c2 is a new node, add it on right
        else:
            heapq.heappush(tree_nodes, TreeNode(c1.val + c2.val, left=c1, right = c2))
    
    # Last node in tree_nodes is root
    root = heapq.heappop(tree_nodes)

    # Traverse the tree to print huffman codes for every character
    huffman_codes = inorderTraversal(root, "")
    return huffman_codes
    

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
    encoded = ""
    for char in st:
        encoded += codes[char]
    print("Encoded String:")
    print(encoded)
    return encoded # To use in part e as bst


# Part d
class unknownHuffmanNode:
    def __init__(self):
        self.char = None
        self.left = None
        self.right = None

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
            elif path == '1':
                if not node.right:
                    node.right = unknownHuffmanNode()
                node = node.right
            else:
                raise ValueError("Huffman codes should be binary!")
        node.char = char 

    return root

# Part e
def Huffman_decode(bst: str, tree: object) -> None:
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

    print("Decoded String:")
    # Traverse the huffman tree to decode each bit in bst until it reaches a leaf node which will be a character.
    for path in bst:
        if path == '0':
            node = node.left
        elif path == '1':
            node = node.right
        else: 
            raise ValueError("Huffman codes should be binary!")
        
        if not node.left and not node.right:
            decoded_string += node.char
            node = root
    
    print(decoded_string)

def main():
    
    st = "abbcccdddd" # Assignment Example
    st2 = "a fast runner need never be afraid of the dark" # Slides Example
    st3 = "" # Edge Case
    
    print("Part a:\nst = \"" + st + "\"")
    frequency_table(st)
    print()
    print("Part a:\nst = \"" + st2 + "\"")
    frequency_table(st2)
    print()
    print("Part a:\nst = \"" + st3 + "\"")
    frequency_table(st3)
    print()
    
    print()

    print("Part b:\nst = \"" + st + "\"")
    st_code = Huffman_code(st)
    print()
    print("Part b:\nst = \"" + st2 + "\"")
    st2_code = Huffman_code(st2)
    print()
    print("Part b:\nst = \"" + st3 + "\"")
    st3_code = Huffman_code(st3)
    print()

    print()

    print("Part c:\nst = \"" + st + "\"")
    st_encoded = Huffman_encode(st, st_code)
    print()
    print("Part c:\nst = \"" + st2 + "\"")
    st2_encoded = Huffman_encode(st2, st2_code)
    print()
    print("Part c:\nst = \"" + st3 + "\"")
    st3_encoded = Huffman_encode(st3, st3_code)
    print()

    print()

    print("part d & e:\nst = \"" + st + "\"")
    codes_list = [('a', '000'), ('b', '001'), ('c', '01'), ('d', '1')]
    tree = Huffman_tree(codes_list)
    Huffman_decode(st_encoded, tree)
    print()

    print("part d & e:\nst = \"" + st2 + "\"")
    codes_list2 = [('r', '000'), ('a', '001'), (' ', '01'), ('t', '1000'), ('f', '1001'), ('e', '101'), ('s', '110000'), ('u', '110001'), ('o', '110010'), ('h', '110011'), ('d', '1101'), ('b', '111000'), ('i', '111001'), ('v', '111010'), ('k', '111011'), ('n', '1111')]
    tree2 = Huffman_tree(codes_list2)
    Huffman_decode(st2_encoded, tree2)
    print()

    print("part d & e:\nst = \"" + st3 + "\"")
    codes_list3 = []
    tree3 = Huffman_tree(codes_list3)
    Huffman_decode(st3_encoded, tree3)

if __name__ == "__main__":
    main()