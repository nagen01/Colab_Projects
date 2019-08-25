# -*- coding: utf-8 -*-
"""
Text Summerizer
Created on Sat Aug 24 09:00:54 2019

@author: Nagendra

"""

#Importing important libraries:
import bs4 as bs
import urllib.request
import re
import heapq
import nltk
nltk.download('stopwords')
nltk.download('punkt')

#Extracting data from website page:
source = urllib.request.urlopen('https://en.wikipedia.org/wiki/Global_warming').read()

#Creating soup 
soup = bs.BeautifulSoup(source,'lxml')

#Extracting the required data in paragraph
text = ""
for paragraph in soup.find_all('p'):
    text += paragraph.text

#Cleaning thedata
text = re.sub(r"\[[0-9]*\]",' ',text)
text = re.sub(r"\s+",' ',text)

clean_text = re.sub(r"\W",' ',text)
clean_text = re.sub(r"\d",' ',clean_text)
clean_text = re.sub(r"\s+",' ',clean_text)
clean_text = clean_text.lower()

#Fining all the stop words in nltk library:
stop_words = nltk.corpus.stopwords.words('english')

#Preparing word2count:
word2count = {}
for word in nltk.word_tokenize(clean_text):
    if word not in stop_words:
        if word not in word2count.keys():
            word2count[word] = 1
        else:
            word2count[word] += 1
            
for key in word2count.keys():
    word2count[key] = word2count[key]/max(word2count.values())

#Sentence tokenize in text form of data where puntuations are still present
sentences = nltk.sent_tokenize(text)

#Preparing sent2count:
sent2score = {}
for sentence in sentences:
    if len(sentence.split(' ')) <= 25:
        for word in nltk.word_tokenize(sentence.lower()):
            if word not in stop_words:
                if word in word2count:
                    if sentence not in sent2score.keys():
                        sent2score[sentence] = word2count[word]
                    else:
                        sent2score[sentence] += word2count[word]

#Fining the best sentences to summerize the whold article
best_sentences = heapq.nlargest(5,sent2score,key=sent2score.get)