import nltk
import re
import heapq

# Download required resources
nltk.download('punkt')
nltk.download('stopwords')

from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize

def generate_summary(text_data, lines=3):
    # Clean up the text
    clean_text = re.sub(r'\[[0-9]*\]', '', text_data)
    clean_text = re.sub(r'\s+', ' ', clean_text)

    # Sentence segmentation
    sentence_list = sent_tokenize(clean_text)

    # Prepare stop words
    stop_words_set = set(stopwords.words("english"))

    # Frequency analysis
    freq_table = {}
    for word in word_tokenize(clean_text.lower()):
        if word.isalnum() and word not in stop_words_set:
            freq_table[word] = freq_table.get(word, 0) + 1

    # Normalize frequencies
    if freq_table:
        max_freq = max(freq_table.values())
        freq_table = {word: count / max_freq for word, count in freq_table.items()}

    # Score sentences
    scored_sentences = {}
    for sent in sentence_list:
        words_in_sent = word_tokenize(sent.lower())
        if len(sent.split()) < 30:
            for word in words_in_sent:
                if word in freq_table:
                    scored_sentences[sent] = scored_sentences.get(sent, 0) + freq_table[word]

    # Select top sentences
    top_sentences = heapq.nlargest(lines, scored_sentences, key=scored_sentences.get)
    summary_result = ' '.join(top_sentences)
    
    return summary_result
