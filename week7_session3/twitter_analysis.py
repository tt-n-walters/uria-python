from nltk.corpus import twitter_samples, stopwords
from ntlk.tokenize import word_tokenizer
from string import punctuation


eng_stopwords = stopwords.words("english")

print(twitter_samples.fileids())
tweets = twitter_samples.strings("tweets.20150430-223406.json")

print(type(tweets))
print(len(tweets))
print(tweets[315])

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
    tokens = word_tokenizer(tweet)
    return tokens

