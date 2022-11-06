from nltk import WordNetLemmatizer
import nltk
import pandas
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def make_lemma(sentence):
    sentence_tokens = nltk.word_tokenize(sentence.lower())
    pos_tags = nltk.pos_tag(sentence_tokens)
    sentence_lemmas = []

    for token, pos_tag in zip(sentence_tokens, pos_tags):
        if pos_tag[1][0].lower() in ["n", "v", "a", "r"]:
            lemma = lemmatizer.lemmatize(token, pos_tag[1][0].lower())
            sentence_lemmas.append(lemma)

    return sentence_lemmas

text = 'Originally, vegetables were collected from the wild by hunter-gatherers. Vegetables are all plants. Vegetables can be eaten either raw or cooked.'
question = 'What are vegetables?' 

lemmatizer = WordNetLemmatizer()

# Split sentences into tokens
sentence_tokens = nltk.sent_tokenize(text)
sentence_tokens.append(question)
print(sentence_tokens)

tv = TfidfVectorizer(tokenizer=make_lemma)
# Counts weight of each word
tf = tv.fit_transform(sentence_tokens)
# print(tf)
# # Returns list of lists - each with the number of elements of longest sentence (articles not included)
# print(tf.toarray())

# If want to see in easier to read table:
df = pandas.DataFrame(tf.toarray(), columns=tv.get_feature_names())
print(df)

# Compare the question (tf[-1]) with tf
# Values will be a list inside a list
values = cosine_similarity(tf[-1], tf)
# Prints an array of values that represents similarity between question and each of the sentences
# Note that the similarity is 1 in last item in array b/c is the question itself (100% similarity)
print(values)

# To find sentence with maximum similarity - gets index of most similar sentence
# argsort returns list inside list because that's what values is, so must indicate index 0
# then indicate index -2 because very last item (aka the most similar) is the original question
index = values.argsort()[0][-2]
print(index)

# To get coefficient of most similar sentence
# Get rid of the nested lists
values_flat = values.flatten()
values_flat.sort()
coeff = values_flat[-2]
print(coeff)

if coeff > 0.3:
    print(sentence_tokens[index])