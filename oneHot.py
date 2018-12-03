import string

def get_unique_word(bulk):
    # split into lines by \n
    lines = bulk.split('\n')
    # prepare a set for words
    words = set()
    # loop through lines
    for line in lines:
        # remove punctuations, lower case, split into list,
        # turn into tuple, and add to words set
        words.update(tuple(line[2:].translate(str.maketrans('','',string.punctuation)).lower().split()))
    return tuple(words)
    
# This function converts a line of our data file into
# a tuple (x, y), where x is #unique_word-dimensional representation
# of the words in a review, and y is its label.
def convert_line_to_example(line, unique_words):
    # Pull out the first character: that's our label (0 or 1)
    y = int(line[0])
    # Split the line into words using Python's split() function
    words = line[2:].translate(str.maketrans('','',string.punctuation)).lower().split()
    # Look up the embeddings of each word, ignoring words not
    # in our pretrained vocabulary.
    embeddings = [0]*len(unique_words)
    for w in words:
        if w in unique_words: # redundunt =_=|||
            embeddings[unique_words.index(w)] += 1
    # Take the mean of the embeddings
    x = np.asarray(embeddings)
    return {'x': x, 'y': y}

# Apply the function to each line in the file.
with open('movie-simple.txt', 'r', encoding = 'utf-8') as f:
    bulk = f.read()
    words = get_unique_word(bulk)
    f.seek(0) # reset the pointer
    dataset = [convert_line_to_example(l, words) for l in f.readlines()]

