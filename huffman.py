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

    #For this problem we literally cannot do anything that isn't O(n)
    #The problem does not assume that it contains numeric or any other characters.
    #For the beginning implementation, let's assume it's just lowercase letters.

    #This simply creates the table
    freq_table = {};

    for letter in range(26):
        freq_table[chr(97+letter)] = 0;
    
    #Loop through the word
    for char in st:
        freq_table[char] += 1
    
    #Print Frequencies once done.
    print("Character Frequencies:\n")

    for key, val in freq_table.items():
        print('\''+key+'\': '+str(val)+'\n');


# Part b
def Huffman_code(st: str) -> None:
    """
    Builds a Huffman tree from the string st and generates the Huffman codes for each character. Print each character with its corresponding code.

    Parameters:
        st (str): A string with a maximum length of 256 characters.
    
    Output:
        Print the Huffman code for each character in the string. 
    """
    print("Huffman Codes:\n'a': 000\n...\n")
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
    frequency_table(st)
    codes = {"a": "000", "b": "001", "c": "01", "d": "1"}
    Huffman_code(st)
    Huffman_encode(st, codes)
    L = [('a', '000'), ('b', '001'), ('c', '01'), ('d', '1')]
    tree = Huffman_tree(L)
    bst = "0000010010010101011111"
    Huffman_decode(bst, tree)

if __name__ == "__main__":
    main()