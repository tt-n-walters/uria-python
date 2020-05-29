from nltk.corpus import twitter_samples

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
    for word in words:
        if word.startswith("@"):
            words.remove(word)
        elif word.startswith("RT"):
            words.remove(word)
        elif word.startswith("http"):
            words.remove(word)
        elif "..." in word or "…" in word:
            words.remove(word)

    # Join the words back together
    tweet = " ".join(words)
    return tweet


print(clean_tweet(tweets[315]))