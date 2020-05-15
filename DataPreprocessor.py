import nltk
from nltk.tokenize import sent_tokenize
import unicodedata
from bs4 import BeautifulSoup
from resources import CONTRACTION_MAP
import re
import spacy

def strip_html_tags(text):
    soup = BeautifulSoup(text, "html.parser")
    stripped_text = soup.get_text()
    return stripped_text

def remove_accented_chars(text):
    text = unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode('utf-8', 'ignore')
    return text

def expand_contractions(text):
    contraction_mapping=CONTRACTION_MAP
    contractions_pattern = re.compile('({})'.format('|'.join(contraction_mapping.keys())), 
                                      flags=re.IGNORECASE|re.DOTALL)
    def expand_match(contraction):
        match = contraction.group(0)
        first_char = match[0]
        expanded_contraction = contraction_mapping.get(match)\
                                    if contraction_mapping.get(match)\
                                    else contraction_mapping.get(match.lower())                       
        expanded_contraction = first_char+expanded_contraction[1:]
        return expanded_contraction
        
    expanded_text = contractions_pattern.sub(expand_match, text)
    expanded_text = re.sub("'", "", expanded_text)
    return expanded_text

def remove_special_characters(text, remove_digits=False):
    
    text = str(text).replace("\n" ,"")
    text = str(text).replace("<br />", " ")
    text = str(text).replace("\''" ,"")
    text = str(text).replace("\\", "")
    text = str(text).replace("()","")
    
    #if(remove_digits):
        #pattern=r'[^a-zA-z\s]'
        #text=re.sub(pattern, '', str(text))
    #else:
        #pattern=r'[^a-zA-z0-9\s]'
        #text=re.sub(pattern, '', str(text))
        # add code for processing digits if any

    return text
    
def split_into_sentences(text):
    nlp = spacy.load('en_core_web_sm')
    docs = nlp(text)
    sentences = list(docs.sents)
    return sentences
    #return text.split('.')
        
def preprocess(text):
    #lowercase
    #text=text.lower()
    #first remove html tags if any
    text=strip_html_tags(text)
    #remove accents
    text=remove_accented_chars(text)
    #full forms
    #text=expand_contractions(text)
    #split into sentences
    list_of_sentences=split_into_sentences(text)
    #removing special characters
    list_of_sentences=list(map(remove_special_characters,list_of_sentences))
    #return the preprocessed list of sentences
    return list_of_sentences