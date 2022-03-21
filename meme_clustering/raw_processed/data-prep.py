import pandas as pd
from tqdm import tqdm 
from utils.PRSR import prsr
import pickle

#list of songs whose comments we will be processing
fn_list = ['J.Balvin_MiGente_118933_2017_es', 'PSY_GangnamStyle_2993360_2012_ko', 'PSY_Gentleman_524723_2013_ko', 'LuisFonsi_Despacito_1631443_2017_es']

kw_list = []
kw_POS_list = []
entire_POS_list = []


def add_to_lists(proc_sents, tags):
    kw_list.append(proc_sents)
    kw_POS = [
        [tag for word, tag in tags[i] if word in proc_sents[i]] 
        for i in range(len(tags))
    ]
    kw_POS_list.append(kw_POS)
    
    POS_list = [
        [tag for word, tag in tags[i]] 
        for i in range(len(tags))
    ]
    entire_POS_list.append(tags)
        

for fn in tqdm(fn_list):
    kw_list = []
    kw_POS_list = []
    entire_pos_list = []

    with open (f"Comment Scraper/Comments/processing/english_lang/{fn}.json", "r", encoding="utf8") as f:
        data = json.load(f)            
    for item in tqdm(data[:-1]):
        #get tokens and POS tags from PRSR
        if item['likes'] >= 1:
            toks, tags = prsr(item['text'], return_POS=True, sent_tokenizer=False)
            kw_list.append(toks)
            entire_pos_list.append(tags)
            #use function to add to lists to avoid repeated codeblock
#                 add_to_lists(proc_sents, tags)

        #repeat above steps for replies
        if 'replies' in item:
            for reply in item['replies']:
                if reply['likes']>=1:
                    toks, tags = prsr(item['text'], return_POS=True, sent_tokenizer=False)
                    kw_list.append(toks)
                    entire_pos_list.append(tags)
#                     add_to_lists(proc_sents, tags)
    df = pd.DataFrame(list(zip(kw_list, entire_pos_list)),
           columns =['KW', 'POS'])
    name = fn.split("_")[1]
    with open (f"saves/memes/raw/{name.lower()}.pickle", "wb") as f:
        pickle.dump(df, f)