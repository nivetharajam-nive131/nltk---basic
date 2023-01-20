import nltk

# Download NLTK's data
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')
nltk.download('vader_lexicon')

# Tokenize text
text = input("Enter a string")
tokens = nltk.word_tokenize(text)
print(tokens)

# Perform stemming and lemmatization
from nltk.stem import PorterStemmer, WordNetLemmatizer
stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()

stemmed_words = [stemmer.stem(word) for word in tokens]
lemmatized_words = [lemmatizer.lemmatize(word) for word in tokens]
print("Stemmed:", stemmed_words)
print("Lemmatized:", lemmatized_words)

# Perform part-of-speech tagging
tagged_words = nltk.pos_tag(tokens)
print(tagged_words)

# Perform sentiment analysis
from nltk.sentiment import SentimentIntensityAnalyzer
analyzer = SentimentIntensityAnalyzer()
score = analyzer.polarity_scores(text)
print(score)
