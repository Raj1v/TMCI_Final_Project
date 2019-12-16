import csv
import sys
import nltk
import pickle
from nltk.corpus import stopwords 
from nltk.corpus import wordnet as wn

csv.field_size_limit(sys.maxsize)

def preprocess_summaries(bills_file_path):
    """Prepropesses summaries of bills from a given congress. Also stores 
        processed bills as a pickle file.

    Args:
        congress: The number of the congress for which bills are wanted

    Returns:
        A list of bills with lemmatized summaries
    """
    id_column = 0
    dataset_topic_column = 2
    summary_column = 3
    
    # Read the bills CSV file
    bills = []
    
    with open(bills_file_path, newline='') as csvfile:
        csvfile.readline()
        rows = csv.reader(csvfile, delimiter='|')
    
        for row in rows:
            bill = dict()
            bill['id'] = row[id_column]
            bill['dataset_topic'] = row[dataset_topic_column]
            bill['summary'] = row[summary_column]
            bills.append(bill)
    
    # Tokenize the bill sumaries
    for bill in bills:
        summary = bill['summary']
        tokenized_summary = nltk.word_tokenize(summary)
        bill['tokenized_summary'] = tokenized_summary
    
    # Lemmatize and filter the summaries
    stop_words = set(stopwords.words('english'))
    
    un2wn_mapping = {"VERB" : wn.VERB, "NOUN" : wn.NOUN, "ADJ" : wn.ADJ, "ADV" : wn.ADV}
    for bill in bills:
        lemmatized_summary = []
        for w, p in nltk.pos_tag(bill['tokenized_summary'], tagset="universal"):
            if p in ["PUNCT"] or w in stop_words:
                continue
            elif p in un2wn_mapping.keys():
                lemma = nltk.WordNetLemmatizer().lemmatize(w, pos = un2wn_mapping[p])
            elif p in ["PROPN"]:
                print(w)
                lemma = nltk.WordNetLemmatizer().lemmatize(w)
    
            lemmatized_summary.append(lemma.lower())  # case insensitive
    
        bill['lemmatized_summary'] = lemmatized_summary
    pickle.dump( bills, open( "lemmatized_bills/" + bills_file_path + ".p", "wb" ) )
    return bills