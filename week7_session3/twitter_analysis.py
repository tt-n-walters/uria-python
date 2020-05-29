from nltk.corpus import twitter_samples, stopwords, wordnet
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
from nltk.stem import WordNetLemmatizer
from string import punctuation

import json
from collections import Counter
import matplotlib.pyplot as plt


eng_stopwords = stopwords.words("english")
lemmatizer = WordNetLemmatizer()
tweets = twitter_samples.strings("tweets.20150430-223406.json")


# Data cleaning
def clean_tweet(tweet):
    # Mentions @
    # RT
    # Links
    # ...
    # Split into words, compare each word and remove if necessary
    words = tweet.split()
    cleaned = []
    for word in words:
        if word.startswith("@"):
            continue
        elif word.startswith("RT"):
            continue
        elif word.startswith("http"):
            continue
        elif "..." in word or "…" in word:
            continue
        # If we want to keep the word
        cleaned.append(word)

    # Join the words back together
    tweet = " ".join(cleaned)
    return tweet


def tokenize(tweet):
    tokens = word_tokenize(tweet)
    return tokens

# Loop over the tokens, only keep those that aren't
# stopwords or punctuation.
def clean_tokens(tokens):
    cleaned = []
    for token in tokens:
        if token in eng_stopwords:
            continue
        if token in punctuation:
            continue
        cleaned.append(token)
    return cleaned


def lemmatize(word, tag):
    if tag.startswith("N"):
        return lemmatizer.lemmatize(word, wordnet.NOUN)
    elif tag.startswith("V"):
        return lemmatizer.lemmatize(word, wordnet.VERB)
    elif tag.startswith("RB"):
        return lemmatizer.lemmatize(word, wordnet.ADV)
    else:
        return lemmatizer.lemmatize(word, wordnet.ADJ)
        
    
file = open("emotions.json")
content = file.read()
file.close()

emotions = json.loads(content)


def count_emotions(tokens):
    counted_emotions = []
    for token in tokens:
        if token in emotions:
            emotion = emotions[token]
            counted_emotions.append(emotion)
    return counted_emotions



tweet = tweets[990]
cleaned = clean_tweet(tweet)
tokens = tokenize(cleaned)
cleaned_tokens = clean_tokens(tokens)
lems = []
for token in cleaned_tokens:
    print(token)
    lems.extend(lemmatize(token, tag))
counted = count_emotions(lems)
frequencies = Counter(counted)

plt.plot(frequencies.keys(), frequencies.values())

print(tweet)
print(cleaned)
print(tokens)
print(cleaned_tokens)