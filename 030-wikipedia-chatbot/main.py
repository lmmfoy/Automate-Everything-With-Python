from nltk import WordNetLemmatizer
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
# nltk.download("averaged_perceptron_tagger")
# nltk.download("wordnet")
# nltk.download("punkt")

text = 'Originally, vegetables were collected from the wild by hunter-gatherers. Vegetables are all plants. Vegetables can be eaten either raw or cooked.'
question = 'What are vegetables?' 

lemmatizer = WordNetLemmatizer()

def make_lemma(sentence):
    sentence_tokens = nltk.word_tokenize(sentence.lower())
    pos_tags = nltk.pos_tag(sentence_tokens)
    sentence_lemmas = []

    for token, pos_tag in zip(sentence_tokens, pos_tags):
        if pos_tag[1][0].lower() in ["n", "v", "a", "r"]:
            lemma = lemmatizer.lemmatize(token, pos_tag[1][0].lower())
            sentence_lemmas.append(lemma)

    return sentence_lemmas

# Split sentences into tokens
sentence_tokens = nltk.sent_tokenize(text)
sentence_tokens.append(question)
print(sentence_tokens)

# Algorithm that finds coefficient that denotes importance of each word
tv = TfidfVectorizer(tokenizer=make_lemma)
tf = tv.fit_transform(sentence_tokens)
# Compare the question (tf[-1]) with tf
values = cosine_similarity(tf[-1], tf)
# To find sentence with maximum similarity - gets index of most similar sentence
index = values.argsort()[0][-2]

# To get coefficient of most similar sentence
# Get rid of the nested lists
values_flat = values.flatten()
values_flat.sort()
coeff = values_flat[-2]

if coeff > 0.3:
    print(sentence_tokens[index])