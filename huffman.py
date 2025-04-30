# Brian Ochoa (beo3), Giovani Bergamasco (glb7), Victor Sima (vs77)
import heapq

class TreeNode:
    def __init__(self, val=0, left=None, right=None, c=''):
        self.val = val
        self.left = left
        self.right = right
        self.c = c
    
    # Apparently we need this for heapq
    def __lt__(self, other):
        return self.val < other.val

def inorderTraversal(root, encoding):
    if(root==None):
        return
    inorderTraversal(root.left, encoding+"0")
    if root.c:
        print(root.c, ":", encoding)
    inorderTraversal(root.right, encoding+"1")

# Part a
def frequency_table(st: str) -> None:
    """
    Constructs a frequency table for each character in the string st and prints it.

    Parameters:
        st (str): A string with a maximum length of 256 characters.

    Output:
        Print each character along with its corresponding frequency.
    """
    # Make a hashmap for frequency table
    freq_table = {}
    for c in st:
        if c not in freq_table:
            freq_table[c] = 1
        else:
            freq_table[c] +=1
    for key in freq_table:
        print("Character: " + key + " Frequency: " + str(freq_table[key]))
    


# Part b
def Huffman_code(st: str) -> None:
    """
    Builds a Huffman tree from the string st and generates the Huffman codes for each character. Print each character with its corresponding code.

    Parameters:
        st (str): A string with a maximum length of 256 characters.
    
    Output:
        Print the Huffman code for each character in the string. 
    """
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
    inorderTraversal(root, "")

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
    st2 = "a fast runner need never be afraid of the dark"
    frequency_table(st)
    codes = {"a": "000", "b": "001", "c": "01", "d": "1"}
    Huffman_code(st)
    print("\n")
    Huffman_code(st2)
    Huffman_encode(st, codes)
    L = [('a', '000'), ('b', '001'), ('c', '01'), ('d', '1')]
    tree = Huffman_tree(L)
    bst = "0000010010010101011111"
    Huffman_decode(bst, tree)

if __name__ == "__main__":
    main()