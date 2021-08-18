import nltk, re, json, os

from nltk.stem.wordnet import WordNetLemmatizer
from nltk.corpus import stopwords
from nltk.tag import pos_tag
from nltk.tokenize import TweetTokenizer

from emoji import UNICODE_EMOJI


import pkg_resources
from symspellpy import SymSpell, Verbosity

from resources.NAMES import names
from resources.contractions import CONTRACTION_MAP
from resources.abbreviations import abbrev_map



def expand_contractions(text, contraction_mapping=CONTRACTION_MAP):
    text = re.sub(r"’", "'", text)
    if text in abbrev_map:
        return(abbrev_map[text])
    text = re.sub(r"\bluv", "lov", text)
    
    contractions_pattern = re.compile('({})'.format('|'.join(contraction_mapping.keys())), 
                                      flags=re.IGNORECASE|re.DOTALL)
    def expand_match(contraction):
        match = contraction.group(0)
        first_char = match[0]
        expanded_contraction = contraction_mapping.get(match)\
                                if contraction_mapping.get(match)\
                                else contraction_mapping.get(match.lower())
        if expanded_contraction != None:
                
            expanded_contraction = first_char+expanded_contraction[1:]
            return expanded_contraction
        else:
            return 0
    try:    
        expanded_text = contractions_pattern.sub(expand_match, text)
        return expanded_text
    except TypeError:
        return 0
    
def reduce_lengthening(text):
    pattern = re.compile(r"(.)\1{2,}")
    return pattern.sub(r"\1\1", text)

def lemmatize_sentence(tokens):
    lemmatizer = WordNetLemmatizer()
    lemmatized_sentence = []
    for word, tag in pos_tag(tokens):
        if tag.startswith('NN'):
            pos = 'n'
        elif tag.startswith('VB'):
            pos = 'v'
        else:
            pos = 'a'
        lemmatized_sentence.append(lemmatizer.lemmatize(word, pos))
    return lemmatized_sentence


def prsr(comments_list):
    if type(comments_list) != list:
        comments_list = [comments_list]
    cleaned = []
    for p_com in comments_list:
        p_com = p_com.lower()
        
        #expand out contractions
        tok = p_com.split(" ")
        z = []
        for w in tok:
            wx = expand_contractions(w)
            if wx == 0:
                continue
            z.append(wx)
        st = " ".join(z)
        
        
        tokenized = tokenizer.tokenize(st)
        reduced = [reduce_lengthening(token) for token in tokenized]
        
        #clean and spellcheck the data
        clean = []
        
        for w in tokenized:
            #spellchecker doesn't like emojis or punctuation (beyond . and ,) so need to filter for them first
            if w in emoji_set:
                clean.append(w)
                continue
            elif re.match(r"[^a-zA-Z]", w):
                continue
            elif w in names:
                clean.append(w)
            else:
                suggestions = sym_spell.lookup(w, Verbosity.CLOSEST,
                               max_edit_distance=0, include_unknown=True)
                sug = str(suggestions[0])
                sug = sug.split(", ")[0]
                clean.append(sug)
                    
                

        cleaned.append(clean)
        
    
    #lemmatize and remove stop words
    lemmatized = [lemmatize_sentence(clean) for clean in cleaned]
    
    stop_words = set(("be", "i", "this", "the", "it", "a", "and", "to", "you", "of", "do", "in", "my", "me", "that", "with", "for", "have", "on"))
    stopped = []
    for lemm in lemmatized:
        stop = [l for l in lemm if l not in stop_words]
        stop2 = [l for l in stop if l not in sw]
    
#         stopped.append(" ".join(stop))
        stopped.append(stop2)
    return stop2


tokenizer = TweetTokenizer(strip_handles=True, reduce_len=True)

sw = set(stopwords.words('english'))

emoji_set = set()
for emoji in UNICODE_EMOJI["en"].keys():
    emoji_set.add(emoji)


sym_spell = SymSpell(max_dictionary_edit_distance=2, prefix_length=7)
dictionary_path = pkg_resources.resource_filename(
    "symspellpy", "frequency_dictionary_en_82_765.txt")

sym_spell.load_dictionary(dictionary_path, term_index=0, count_index=1)

if __name__ == "__main__":
    pass
