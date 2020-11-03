
from nltk.corpus import movie_reviews
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk import pos_tag
import string



clitics = open('clitics', 'r').readlines()

sents0 = movie_reviews.words("neg/cv000_29416.txt")
sents1 = movie_reviews.words("pos/cv041_21113.txt")



texts2 = sents0 + sents1


# ################################################
# Remove all newline characters.
    
def RemoveAllNewline():
    a1 = []
    a1 = string.splitlines(texts2)
    return a1

# ################################################
# Replace HTML character codes (i.e., &...;) with whitespace.
    
def ReplaceHTMLCharacters():
    a=[]
    for w in texts2:
        a.append(re.sub('<*?&;>', ' ', w))
    return a


#################################################
# Remove all URLs .

def RemoveAllURLs():
    b = []    
    for w in ReplaceHTMLCharacters():
        b.append(re.sub(r'^https?://.*[\r\n]*', '', w))
    return b


#################################################
#Split each punctuation (using library called string to detectpunctuation symbols) into its own token using whitespace

def SplitEachPunctuation():
    c = []
    punct=[string.punctuation]
    for item in RemoveAllURLs():
        if item not in punct:
           c.append(item)
    return c
       
################################################
#Split clitics using whitespace (see clitics file in the section materials).

def SplitClitics():
    d =[]
    for item in SplitEachPunctuation():
        for i in clitics:
            d.append(re.sub(i, ' ' + i, item))        
    return d


################################################
# Remove stopwords.

def RemoveStopwords():
    e = []
    stop_words = set(stopwords.words("english"))

    for item in SplitClitics():
        if item not in stop_words:
           e.append(item)
    return e
#################################################
#Each token is tagged with its part-of-speech using nltk tagger .
    
def pos():
    f = []
    for t in RemoveStopwords():    
        f = word_tokenize(t)
        f.append(pos_tag(t))
    return f
#################################################
# Apply lemmatization using nltk.

def lemmatization():
    g = []
    for w in RemoveStopwords():
        lemma = WordNetLemmatizer().lemmatize(w, pos='n')
        g.append(lemma)
    return g

#################################################
# Convert text to lowercase.
    
def lowCase():
    h = []
    for w in RemoveStopwords():
        h.append(w.lower())
        
    return h
##################################################
    


print(lowCase())    
