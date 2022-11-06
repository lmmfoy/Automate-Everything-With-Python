from nltk import WordNetLemmatizer
import nltk
# nltk.download('omw-1.4')
# nltk.download('wordnet')
# For tokenization:
# nltk.download("punkt")
# nltk.download("pos_tag")

x = "was"
y = "is"

lemmatizer = WordNetLemmatizer()
# lemmatize(word, part-of-speech tag)
lemma1 = lemmatizer.lemmatize(x, "v")
lemma2 = lemmatizer.lemmatize(y, "v")
print(lemma1 == lemma2)

# Tokenization is better than .split because takes punctuation into consideration -- more accurate
tokens = nltk.word_tokenize("The cats ran down the alley in a frenzied way".lower())
print(tokens)

# Note: "I" is code for preposition, "R" for adverbs
# Returns tuples (token, tag) - 1st character of tag string refers to N/V/I/R/A
pos_tags = nltk.pos_tag(tokens)
print(pos_tags)

sentence_lemmas = []
for token, pos_tag in zip(tokens, pos_tags):
    # For pos_tag, want 2nd item in tuple and 1st item of tag string (needs to be lowercase)
    # Prepositions, punctuation don't have lemmas, have to filter them out
    if pos_tag[1][0].lower() in ["n", "v", "a", "r"]:
        lemma = lemmatizer.lemmatize(token, pos_tag[1][0].lower())
        sentence_lemmas.append(lemma)

print(sentence_lemmas)
