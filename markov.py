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


    words = text_string.split()


    word_dict = {}

    for i in range(len(words) - 2):

        key = (words[i], words[i + 1])
        word = words[i + 2]

        if key not in word_dict:
            word_dict[key] = []

        word_dict[key].append(word)


    return word_dict




def make_text(chains):
    """Takes dictionary of markov chains; returns random text."""

#Concatenate string from key with randomly chosen string from values, creating a new string
#Do we store each link in a list and then join the strings?  Or keep concatenating into one string?
    


    key = choice(chains.keys())

    text = key[0] + " " + key[1] + " " 
    
    while key in chains:

        next_word = choice(chains[key])
        text += next_word + " "
        key = (key[1], next_word)

    return text













input_path = "green-eggs.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print random_text

