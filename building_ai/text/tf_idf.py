import numpy as np
import string

text = '''Humpty Dumpty sat on a wall
Humpty Dumpty had a great fall
all the king's horses and all the king's men
couldn't put Humpty together again'''

text4 = '''11111 11110 11101 11100 11011 
11001 11000 1 10111 111 10101
10011 10010 1 10001 10000 01111
01101 01100 01011 1 01010 01001
111 00110 1 00101 1000 00011
00001 111'''

def idf(word, docs):
    return np.log10(len(docs) / sum([1.0 for doc in docs if word in doc]))

def calculate_idf_vector(unique_words, docs):
    idf_vector = np.zeros((len(unique_words)), dtype=float)
    for i in range(len(unique_words)):
        idf_vector[i] = idf(unique_words[i], docs)
    return idf_vector

def calculate_tf_vector(unique_words, doc):
    tf_vector = np.zeros((len(unique_words)), dtype=float)
    for i in range(len(unique_words)):
        tf_vector[i] = doc.count(unique_words[i]) / len(doc)
    return tf_vector

def dist_manhattan(a, b):
    return np.sum(np.abs(np.array(a) - np.array(b)))

def main(text):
    # tasks your code should perform:

    # 1. split the text into words, and get a list of unique words that appear in it
    # a short one-liner to separate the text into sentences (with words lower-cased to make words equal 
    # despite casing) can be done with
     
    # filtered_text = text.translate(str.maketrans('', '', string.punctuation))
    # docs = [line.lower().split() for line in filtered_text.split('\n')]

    docs = [line.lower().split() for line in text.split('\n')]

    print("docs: ", docs)

    unique_words = []
    [unique_words.append(word) for line in docs for word in line if word not in unique_words]

    print("unique_words: ", unique_words)

    print("len(unique_words): ", len(unique_words))
    
    #print("index of 'wall': ", unique_words.index('wall'))

    word_vector = np.zeros((len(docs), len(unique_words)), dtype=float)

    print("word_vector: \n", word_vector)

    idf_vector = calculate_idf_vector(unique_words, docs)

    print("idf_vector: ", idf_vector)

    for i in range(len(docs)):
        word_vector[i] = calculate_tf_vector(unique_words, docs[i]) * idf_vector
    
    print("word_vector: \n", word_vector)

    N = len(word_vector)
    print("N: ", N)

    dist = np.empty((N, N), dtype=float)
    dist.fill(np.inf)

    for x in range(N):
        for y in range(N):
            if x == y:
                continue
            dist[x, y] = dist_manhattan(word_vector[x], word_vector[y])
            print("x: ", x, "y: ", y, "dist: ", dist[x, y])
    
    print("dist: \n", dist)
    print("np.argmin(dist): ", np.argmin(dist))
    print(np.unravel_index(np.argmin(dist), dist.shape))
    pos = np.unravel_index(np.argmin(dist), dist.shape)
    print("pos: ", pos)
    print("docs[pos[0]]: ", docs[pos[0]])
    print("docs[pos[1]]: ", docs[pos[1]])


    # 2. go over each unique word and calculate its term frequency, and its document frequency

    # 3. after you have your term frequencies and document frequencies, go over each line in the text and 
    # calculate its TF-IDF representation, which will be a vector

    # 4. after you have calculated the TF-IDF representations for each line in the text, you need to
    # calculate the distances between each line to find which are the closest.


main(text)