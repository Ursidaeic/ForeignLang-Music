# Exploring the reception of foreign language music in the English-speaking world 
This repository contains the main tools that I developed for my research project into the way the public recieves foreign language music on YouTube. It provides scripts for downloading YouTube comments from the YouTube API, scraping and processing charts data, filtering comments based off content and language, and a novel methodology for clustering memes using cosine similarity and syntactic features in tandem.

## Getting started
I have elected to group all the tools into one project folder as one script will tend to rely on data produced by the previous. Consequently, I have provided one requirements.txt for the entire project, which can be installed with the following command:
```bash
pip install -r requirements.txt 
```
One noteable exception is the PyCLD2 language detection package which is used in the [opinion_miner](https://github.com/Ursidaeic/ForeignLang-Music/tree/main/opinion_miner)  and [forlang_song_identifier](https://github.com/Ursidaeic/ForeignLang-Music/tree/main/forlang_song_identifier) folders. I had trouble installing this with pip, and so to work around this installed it directly from the binary, which can be found [here](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pycld2). 

## Datasets
If you wish to make use of the datasets I coallated instead of producing your own, they can all be found in [this Google Drive](https://drive.google.com/drive/folders/1f6OK0lZTwU937JwAzNPQXyRbNwlp8XxZ?usp=sharing). Here you will find the full comments lists, the subsequent English-language filtered comments, and finally the English-language comments that have been further filtered for opinion-containing comments. Additionally, all the datasets associated with the [meme clustering](https://github.com/Ursidaeic/ForeignLang-Music/tree/main/meme_clustering) methodology - most notably the final .gexf graphs visualising the clusters - can be found in the memes_datasets zip. 

## Contact
If you wish to contact me regarding any of the tools, techniques, or datasets contained within this project, you can do so at charlie.c.armstead@gmail.com
