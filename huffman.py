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
def Huffman_code(st: str) -> None:
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
            heapq.heappush(nTree_nodes, HuffmanNode(None, merged_freq, right_subtree, left_subtree))
        else:
            heapq.heappush(nTree_nodes, HuffmanNode(None, merged_freq, left_subtree, right_subtree))

    root = nTree_nodes.pop();
    huffman_code = tree_traversal(root, "", {}, None)
    print(huffman_code)
    #print("Huffman Codes:\n'a': 000\n...\n")


def tree_traversal(root:HuffmanNode, encoding: str, e_table: dict, parent: tuple):
    if root is None:
        return e_table


    tree_traversal(root.left, encoding+"0", e_table, parent)

    if root.char is not None:
        e_table[root.char] = encoding
        return e_table

    tree_traversal(root.right, encoding+"1", e_table, parent)

    return e_table

   

# Part c
def Huffman_encode(st: str, codes: dict) -> None:
    """
    Prints the binary encoded version of st, based on the Huffman codes generated in part (b) codes.

    Parameters:
        st (str): A string with a maximum length of 256 characters.
        codes: Huffman codes codes.

    Output:
        Print the binary-encoded string using the Huffman codes. 
    """
    print("Encoded String:\n0000010010010101011111\n")


# Part d
def Huffman_tree(L: list):
    """
    Given a list L of characters and their corresponding Huffman codes; construct a Huffman tree based on this list.

    Parameters:
        L (list): A list L of characters and their corresponding Huffman codes.

    Output:
        Return the Huffman tree constructed from the list. 
    """
    pass

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
    print("Decoded String:\nabbccdddd")

def main():
    st = "abbcccdddd"
    test_str = "aaabbbbbccdddddddd"
    frequency_table(st)
    frequency_table(test_str)
    codes = {"a": "000", "b": "001", "c": "01", "d": "1"}
    Huffman_code(st)
    Huffman_code(test_str)
    Huffman_encode(st, codes)
    L = [('a', '000'), ('b', '001'), ('c', '01'), ('d', '1')]
    tree = Huffman_tree(L)
    bst = "0000010010010101011111"
    Huffman_decode(bst, tree)

if __name__ == "__main__":
    main()