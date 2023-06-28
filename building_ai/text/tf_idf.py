import numpy as np

text = '''Humpty Dumpty sat on a wall
Humpty Dumpty had a great fall
all the king's horses and all the king's men
couldn't put Humpty together again'''

def idf(word, docs):
    return np.log(len(docs) / sum([1.0 for doc in docs if word in doc]))

def calcuate_idf_vector(unique_words, docs):
    idf_vector = np.zeros((len(unique_words)), dtype=float)
    for i in range(len(unique_words)):
        idf_vector[i] = idf(unique_words[i], docs)
    return idf_vector


def main(text):
    # tasks your code should perform:

    # 1. split the text into words, and get a list of unique words that appear in it
    # a short one-liner to separate the text into sentences (with words lower-cased to make words equal 
    # despite casing) can be done with 
    docs = [line.lower().split() for line in text.split('\n')]

    print("docs: ", docs)

    unique_words = []
    [unique_words.append(word) for line in docs for word in line if word not in unique_words]

    print("unique_words: ", unique_words)

    print("len(unique_words): ", len(unique_words))
    
    print("index of 'wall': ", unique_words.index('wall'))

    word_vector = np.zeros((len(docs), len(unique_words)), dtype=float)

    print("word_vector: \n", word_vector)

    idf_vector = calcuate_idf_vector(unique_words, docs)

    print("idf_vector: ", idf_vector)

    # 2. go over each unique word and calculate its term frequency, and its document frequency

    # 3. after you have your term frequencies and document frequencies, go over each line in the text and 
    # calculate its TF-IDF representation, which will be a vector

    # 4. after you have calculated the TF-IDF representations for each line in the text, you need to
    # calculate the distances between each line to find which are the closest.


main(text)