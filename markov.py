from random import choice


def open_and_read_file(file_path):
    """Takes file path as string; returns text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    full_text = open(file_path).read()

    #print full_text

    return full_text

# open_and_read_file("green-eggs.txt")

def make_chains(text_string):
    """Takes input text as string; returns _dictionary_ of markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> make_chains("hi there mary hi there juanita")
        {('hi', 'there'): ['mary', 'juanita'], ('there', 'mary'): ['hi'], ('mary', 'hi': ['there']}
    """
#Create list of words, split on empty white space
#Create tuple pairs as keys (starting at first 2), then shifting over 1
#Add appropriate list of values based on tuple pair
#Add all key-value pairs to an empty dictionary

    words = text_string.split()


    word_dict = {}

    for i in range(len(words)-2):

        key = (words[i], words[i+1])
        word = words[i+2]

        if key not in word_dict.keys():
            word_dict[key] = []

        word_dict[key].append(word)


    return word_dict




def make_text(chains):
    """Takes dictionary of markov chains; returns random text."""

    text = ""

    # your code goes here

    return text


input_path = "green-eggs.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print random_text