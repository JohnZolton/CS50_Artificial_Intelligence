import nltk
import sys
import os
import string
import math

FILE_MATCHES = 1
SENTENCE_MATCHES = 1


def main():

    # Check command-line arguments
    if len(sys.argv) != 2:
        sys.exit("Usage: python questions.py corpus")

    # Calculate IDF values across files
    files = load_files(sys.argv[1])
    file_words = {
        filename: tokenize(files[filename])
        for filename in files
    }
    file_idfs = compute_idfs(file_words)

    # Prompt user for query
    query = set(tokenize(input("Query: ")))

    # Determine top file matches according to TF-IDF
    filenames = top_files(query, file_words, file_idfs, n=FILE_MATCHES)

    # Extract sentences from top files
    sentences = dict()
    for filename in filenames:
        for passage in files[filename].split("\n"):
            for sentence in nltk.sent_tokenize(passage):
                tokens = tokenize(sentence)
                if tokens:
                    sentences[sentence] = tokens

    # Compute IDF values across sentences
    idfs = compute_idfs(sentences)

    # Determine top sentence matches
    matches = top_sentences(query, sentences, idfs, n=SENTENCE_MATCHES)
    for match in matches:
        print(match)


def load_files(directory):
    """
    Given a directory name, return a dictionary mapping the filename of each
    `.txt` file inside that directory to the file's contents as a string.
    """
    content = {}
    
    for file in os.scandir(directory):
        if file.is_file():
            with open(file, encoding = "utf-8") as f:
                filename = os.path.split(file)[1]
                contents = f.read()
                content[filename] = contents
    
    return content
    

def tokenize(document):
    """
    Given a document (represented as a string), return a list of all of the
    words in that document, in order.

    Process document by coverting all words to lowercase, and removing any
    punctuation or English stopwords.
    """
    
    document = document.lower()
    words = nltk.tokenize.word_tokenize(document)

    for word in words:
        if word in string.punctuation or word in nltk.corpus.stopwords.words("english"):
            words.remove(word)

    return words


def compute_idfs(documents):
    """
    Given a dictionary of `documents` that maps names of documents to a list
    of words, return a dictionary that maps words to their IDF values.

    Any word that appears in at least one of the documents should be in the
    resulting dictionary.
    """
    wordfreq = {}
    
    for document in documents.keys(): # check each document
        # get a list of unique words in each document
        uniquewords = []
        for word in documents[document]: # check each word in the document
            #we only care about the first occurrence of the word for IDF
            if word not in uniquewords: 
                uniquewords.append(word)
        
        for uword in uniquewords:
            if uword not in wordfreq:
                wordfreq[uword] = 1
            else:
                wordfreq[uword] += 1
            
    # now we have words and their frequencies
    # inverse document frequency = ln(TotalDocs / #DocsContaining(word))
    idfs = {}
    totaldocs = len(documents.keys())

    for word in wordfreq:
        docscontaining = wordfreq[word]
        idfs[word] = math.log(totaldocs/docscontaining)
    # the rarer a word is the higher its IDF value will be
    return idfs
    

def top_files(query, files, idfs, n):
    """
    Given a `query` (a set of words), `files` (a dictionary mapping names of
    files to a list of their words), and `idfs` (a dictionary mapping words
    to their IDF values), return a list of the filenames of the the `n` top
    files that match the query, ranked according to tf-idf.
    """
    # initial idf scores to 0
    scores = {}
    for name in files:
        scores[name] = 0
    
    for doc in files:
        for word in files[doc]:
            if word in query:
                scores[doc] += idfs[word]

    ans = sorted(scores.items(), key=lambda x:x[1], reverse=True)

    res = []
    for i in range(n):
        res.append(ans[i][0])

    return res


def top_sentences(query, sentences, idfs, n):
    """
    Given a `query` (a set of words), `sentences` (a dictionary mapping
    sentences to a list of their words), and `idfs` (a dictionary mapping words
    to their IDF values), return a list of the `n` top sentences that match
    the query, ranked according to idf. If there are ties, preference should
    be given to sentences that have a higher query term density.
    """
    scores = [] # (Sentence, IDF value, query term density)

    for sentence in sentences:
        count = 0
        idf = 0
        for word in list(query): # cycle through words in the query to avoid double counting
            if word in sentences[sentence]: 
                idf += idfs[word]
                count += 1
        qtd = count / len(sentence)
        if qtd > 0 and idf > 0:
            scores.append((sentence, idf, qtd))
    
    ans = sorted(scores, key=lambda x:x[1], reverse = True)
    
    #check and resolve any ties according to query term density
    for i in range(len(ans)-1):
        if ans[i][1] == ans[i+1][1]:
            if ans[i+1][2] > ans[i][2]:
                ans[i], ans[i+1] = ans[i+1], ans[i]
            
    res = []
    for i in range(n):
        res.append(ans[i][0])
    return res


if __name__ == "__main__":
    main()
