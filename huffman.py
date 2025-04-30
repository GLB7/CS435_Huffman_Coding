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
class Node:
    def __init__(self, char, freq):
        self.char  = char # Leaf nodes = symbol / char | Intenral nodes = None
        self.freq  = freq
        self.left  = None
        self.right = None

    # “<” so heapq can compare nodes (by frequency) when pushing/popping to heapify
    def __lt__(self, other):
        return self.freq < other.freq
    
    # Uses DFS to get the huffman codes
    def getHuffmanCodes(self, current_code="", codes=None):
        # For first instance to initialize the codes dictionary
        if codes is None:
            codes = {}

        # Base case (It's a leaf node, an actual character)
        if self.char is not None:
            if current_code == "": # If the tree has only one symbol
                codes[self.char] = "0"
            else:
                codes[self.char] = current_code
        else:
            if self.left is not None:
                self.left.getHuffmanCodes(current_code + "0", codes) # Every left traversal is a 0
            if self.right is not None:
                self.right.getHuffmanCodes(current_code + "1", codes) # Every right traversal is a 1
        
        return codes

def Huffman_code(st: str) -> None:
    """
    Builds a Huffman tree from the string st and generates the Huffman codes for each character. Print each character with its corresponding code.

    Parameters:
        st (str): A string with a maximum length of 256 characters.
    
    Output:
        Print the Huffman code for each character in the string. 
    """
    # Build Table Again
    frequency_table: dict[str, int] = {}
    for char in st:
        if char in frequency_table:
            frequency_table[char] += 1
        else:
            frequency_table[char] = 1

    # Build a heap
    heap = []
    for char in frequency_table:
        freq = frequency_table[char]
        node = Node(char, freq)
        heapq.heappush(heap, node)
    
    # For testing / learning
    # A valid min heap has: left child at index 2i + 1 : right child at index 2i + 2
    print("heap =", [(n.char, n.freq) for n in heap])

    while len(heap) > 1:
        # Extract 2 smallest frequencies from the heap (left & right)
        right = heapq.heappop(heap)
        left  = heapq.heappop(heap)
        parent = Node(None, right.freq + left.freq) # char is None here for the internal node.
        parent.right, parent.left = right, left
        heapq.heappush(heap, parent) # put parent back into the heap with the updated frequency. (heap is always shrinking by 2 and growing by 1)
        # Visaul of heap being built (also for testing / learning)
        print("heap =", [(n.char, n.freq) for n in heap])

    root = heapq.heappop(heap) # This is the huffman tree!!!
    huffman_codes = root.getHuffmanCodes()

    # Print the characters from the frequency table in sorted order (based on char).
    print("\nHuffman Codes:")
    for ch in sorted(huffman_codes):
        print(f"{repr(ch)}: {huffman_codes[ch]}")

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
    print("Encoded String:\n")

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
    print("Decoded String:\n")

def main():
    
    st = "abbcccdddd" # Assignment Example
    st2 = "a fast runner need never be afraid of the dark" # Slides Example
    print("Part a:\nst = \"" + st + "\"")
    frequency_table(st)
    print("Part a:\nst = \"" + st2 + "\"")
    frequency_table(st2)
    print("Part b:\nst = \"" + st + "\"")
    Huffman_code(st)
    print("Part b:\nst = \"" + st2 + "\"")
    Huffman_code(st2)

if __name__ == "__main__":
    main()