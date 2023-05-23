from http.client import responses
import random
import json
import pickle
import numpy as np
import nltk
from nltk.stem import WordNetLemmatizer

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation, Dropout
from tensorflow.keras.optimizers import SGD

lemmatizer = WordNetLemmatizer

intents =json.loads(open('responses.json').read())

words= []
classes= []
documments= []
ignore_letters = ['?', '!','.', ',']

for response in responses['intents']:
    for pattern in responses['patterns']:
        word_list = nltk.tokenize(pattern)
        words.append(word_list)
