import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
# nltk.download("vader_lexicon")
# nltk.download("twitter_samples")

analyzer = SentimentIntensityAnalyzer()

text1 = "What a beautiful day! How amazing it is!"

# Shows scores for "neg", "neu", "pos", "compound" - the sum of the first 3 coefficients is always equal to 1
# The closer the compound is to 1, the more positive it is
scores = analyzer.polarity_scores(text1)

if scores["compound"] > 0:
    print("Positive text")
else:
    print("Negative text")

# Can use a corpus of twitter samples provided by nltk
tweet1 = nltk.corpus.twitter_samples.strings()[0]
tweet2 = nltk.corpus.twitter_samples.strings()[54]
tweet3 = nltk.corpus.twitter_samples.strings()[182]


print(tweet1, analyzer.polarity_scores(tweet1))
print(tweet2, analyzer.polarity_scores(tweet2))
print(tweet3, analyzer.polarity_scores(tweet3))