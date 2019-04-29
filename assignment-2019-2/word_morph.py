from collections import deque
from b_tree import BKTree

import sys
import string


def wagner_fisher(s, t):
    m, n = len(s), len(t)
    d = [range(n+1)]
    d += [[i] for i in range(1,m+1)]
    for i in range(0,m):
        for j in range(0,n):
            cost = 1
            if s[i] == t[j]: cost = 0

            d[i+1].append( min(d[i][j+1]+1, # deletion
                               d[i+1][j]+1, #insertion
                               d[i][j]+cost) #substitution
                           )
    return d[m][n]

def preprocess_input(s):

    # Takes a input and removes the punctuation's from the string.

    # :param s: the string to preprocess.
    # :return: returns the processed string.

    for p in string.punctuation:
        s = s.replace(p, '')

    return s.lower().strip()

def dict_words(dictfile="word_dict.txt"):
    "Return an iterator that produces words in the given dictionary."
    return filter(len,
                map(str.strip,
                        open(dictfile)))

def brute_query(word, words, distfn, n):
    """A brute force distance query
    Arguments:
    word: the word to query for
    words: a iterable that produces words to test
    distfn: a binary function that returns the distance between a
    `word' and an item in `words'.
    n: an integer that specifies the distance of a matching word
    
    """
    return [i for i in words
            if distfn(i, word) <= n]

def main():
    d = deque([])
    start_word = ""
    end_word = ""
    if len(sys.argv) == 4:
        if sys.argv[0] == "word_morph.py" and (sys.argv[1])[-3:] == "txt":
            start_word = sys.argv[2]
            end_word = sys.argv[3]
            with open('word_dict.txt', 'r') as fin:
                d.append(fin.read())
    
    tree = BKTree(wagner_fisher, dict_words())
    

if __name__ == "__main__":
    print("main function..")
    main()