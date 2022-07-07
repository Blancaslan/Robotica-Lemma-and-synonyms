from nltk.stem import WordNetLemmatizer
# function to lemmatize
def Lemma(word, context):
    lemmatizer = WordNetLemmatizer()
    lemma_word = lemmatizer.lemmatize(word, context)
    return lemma_word