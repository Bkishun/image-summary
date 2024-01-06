import nltk
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.probability import FreqDist
from nltk.tokenize.treebank import TreebankWordDetokenizer

nltk.download('punkt')
nltk.download('stopwords')

def get_frequency_distribution(text):
    words = word_tokenize(text.lower())
    stop_words = set(stopwords.words("english"))
    filtered_words = [word for word in words if word.isalnum() and word not in stop_words]
    frequency_distribution = FreqDist(filtered_words)
    return frequency_distribution

def summarize(text, num_sentences=3):
    sentences = sent_tokenize(text)
    frequency_distribution = get_frequency_distribution(text)

    # Assign scores to sentences based on word frequency
    scores = {sentence: sum(frequency_distribution[word] for word in word_tokenize(sentence.lower()) 
                            if word.isalnum()) for sentence in sentences}

    selected_sentences = sorted(sentences, key=lambda sentence: scores[sentence], reverse=True)[:num_sentences]

    # Detokenize selected sentences to form the summary
    summary = TreebankWordDetokenizer().detokenize(selected_sentences)
    return summary