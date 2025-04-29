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
    # This string example is from slide 36
    st = "a fast runner need never be afraid of the dark"
    frequency_table(st)

if __name__ == "__main__":
    main()