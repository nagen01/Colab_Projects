# -*- coding: utf-8 -*-
"""
Word2Vec analysis
Created on Sat Aug 24 16:50:36 2019

@author: Nagendra
"""
#Importing important libraries
import nltk
nltk.download('stopwords')
import re
from gensim.models import Word2Vec
import bs4 as bs
import urllib.request

source = urllib.request.urlopen('https://en.wikipedia.org/wiki/Global_warming').read()

soup = bs.BeautifulSoup(source,'lxml')

text = ""
for paragraph in soup.find_all('p'):
    text += paragraph.text
    
text = re.sub(r"[\[0-9]*\]"," ",text)
text = re.sub(r"\s+"," ",text)

text = text.lower()
text = re.sub(r"[@#$%^&\*\.\-\?\<\>\:\;\'\"\/\(\)\!\~\,]"," ",text)
text = re.sub(r"\W"," ",text)
text = re.sub(r"\d"," ",text)
text = re.sub(r"\s+"," ",text)

sentences = nltk.sent_tokenize(text)
sentences = [nltk.word_tokenize(sentence) for sentence in sentences]
for i in range(len(sentences)):
    sentences[i] = [word for word in sentences[i] if word not in nltk.corpus.stopwords.words('english')]

model = Word2Vec(sentences,min_count=1)

words = model.wv.vocab
vector = model.wv['global']

similar = model.wv.most_similar('earth')


