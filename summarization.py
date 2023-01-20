import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.probability import FreqDist

# Download NLTK's data
nltk.download('punkt')
nltk.download('stopwords')

# Get the text from the user
text = input("Enter the text to be summarized: ")

# Tokenize the text into sentences
sentences = sent_tokenize(text)

# Tokenize the sentences into words
words = [word_tokenize(sentence) for sentence in sentences]

# Remove stop words
stop_words = set(stopwords.words('english'))
filtered_words = [[word for word in sentence if word.lower() not in stop_words] for sentence in words]

# Create a frequency distribution of the remaining words
fdist = FreqDist(word.lower() for sentence in filtered_words for word in sentence)

# Extract the most frequent words and phrases
n = int(input("Enter the number of most frequent words to include in the summary: "))
most_common = fdist.most_common(n)

# Create a summary by extracting the sentences that contain the most frequent words
summary = []
for sentence in sentences:
    for word, freq in most_common:
        if word in sentence:
            summary.append(sentence)
            break

# Print the summary
print("Summary:")
print(" ".join(summary))
