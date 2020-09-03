#!/usr/bin/env python
# coding: utf-8

# In[1]:


import nltk
from nltk.collocations import *
from nltk import pos_tag
from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk import FreqDist
import glob
files = glob.glob("C:\\Users\\Shiva\\textfiles\\*.txt")


# In[2]:


for name in files:
            try:
                with open(name) as f:
                    # to read the text file.
                    contents = f.read()
                    lower_text = contents.lower()
                # converts the entire text into words.
                    word_tokens = nltk.word_tokenize(lower_text)
                    stopword = stopwords.words('english')
                # removes the punctuations and few other grammar.
                    removing_stopwords = [word for word in word_tokens if word not in stopword]
                # convert similar words into certain word example:drove,driven,drives to drive.
                    wordnet_lemmatizer = WordNetLemmatizer()
                    lemmatized_word = [wordnet_lemmatizer.lemmatize(word) for word in word_tokens]
                # it counts the number of repeations of the certain word.
                    word_freq = FreqDist(word_tokens)
                # it basically tags the phrase of the word.
                    pos_tag = nltk.pos_tag(lemmatized_word)
                # separating only nouns of entire tags.
                    length = len(pos_tag) - 1
                    wb = str(name) + "_output"
                    f = open('%s.csv' % name, 'wb')
                    for i in range(0, length):
                        nag = (pos_tag [i][1][0] == 'N')
                        if nag == True:
                            print(pos_tag [i][0])
                    #noun_word_freq = FreqDist(nouns)
                    print(f)
            except IOError as exc:
                if exc.errno != errno.EISDIR:
                    raise
                None


# In[3]:


for name in files:
            try:
                with open(name) as f:
                    # to read the text file.
                    contents = name
                    lower_text = contents.lower()
                # converts the entire text into words.
                    word_tokens = nltk.word_tokenize(lower_text)
                    stopword = stopwords.words('english')
                # removes the punctuations and few other grammar.
                    removing_stopwords = [word for word in word_tokens if word not in stopword]
                # convert similar words into certain word example:drove,driven,drives to drive.
                    wordnet_lemmatizer = WordNetLemmatizer()
                    lemmatized_word = [wordnet_lemmatizer.lemmatize(word) for word in word_tokens]
                # it counts the number of repeations of the certain word.
                    word_freq = FreqDist(word_tokens)
                # it basically tags the phrase of the word.
                    pos_tag = nltk.pos_tag(lemmatized_word)
                # separating only nouns of entire tags.
                    length = len(pos_tag) - 1
                    wb = str(name) + "_output"
                    fa = open('%s.csv' % name, 'wb')
                    for i in range(0, length):
                        nag = (pos_tag [i][1][0] == 'N')
                        if nag == True:
                            print(pos_tag [i][0])
                    #noun_word_freq = FreqDist(nouns)
                    print(fa)
            except IOError as exc:
                if exc.errno != errno.EISDIR:
                    raise
                None


# In[10]:


import pandas as pd
import glob
import os
import numpy as np
#as an example I took a 4 csv files and made a comparsion it worked 
sample1 = pd.read_csv('C:\\Users\\sample1.csv')
sample2 = pd.read_csv('C:\\Users\\sample2.csv')
sample3 = pd.read_csv('C:\\Users\\Public\\sample3.csv')
sample4 = pd.read_csv('C:\\Users\\Public\\sample4.csv')
x = [sample1,sample2,sample3] # forming an array of files 
y = [sample3+sample2,sample4]
for comp in x:
    for comp2 in y:
        print(comp, comp2,np.isin(comp,comp2))


# In[11]:



# I'm planning to place the title nouns files in certain place so that it is eassy to give a path 
titlepath = r'C:\Users'
# I'm planning to place the text nouns files in other place so that it is eassy to give a path 
textpath = r'C:\Users\Public'

title_files = glob.glob(os.path.join(titlepath, "*.csv"))
text_files = glob.glob(os.path.join(textpath, "*.csv"))


df_title_from_each_file = (pd.read_csv(f) for f in title_files)
df_text_from_each_file = (pd.read_csv(fa) for fa in text_files)
x = [df_title_from_each_file] # basically here it should be the extracted title nouns files 
y = [df_text_from_each_file]  # basically here it should be the extracted text nouns files 
# the issue is it reading the files but it should form like an array which is not happening so this is second issue to look up.
for comp in x:
    for comp2 in y:
        print(comp, comp2,np.isin(comp,comp2))


# In[ ]:





# In[ ]:




