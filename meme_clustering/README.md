# A tool for clustering similar strings based off content and part-of-speech tags
This tool will take an array of strings stored as a Pandas DataFrame, in this case YouTube comments, and cluster them based off of whether there is a common part-of-speech (POS) sequence and the content of the strings.
There are three programs contained in this project folder. 
The first, "data_prep.py" will prepare lists of strings downloaded from the YouTube API with [this](https://github.com/Ursidaeic/ForeignLang-Music/tree/main/comment_scraper) tool placed in the comments directory.
This preparation entails removing extraneous infomration (eg., author, time of publication) and threshholding comments based off the like-count it has received. 
The reason for the latter was due to limits regarding computing-costs of the project and you may wish to bypass this step if this is not a concern for you.
I have decided to leave the specific threshholding information that I made use of in the .py file to serve as an example, and this will require changing.
memes_sim.py is the script that actually calculates the similarities between all the comments in the list and returns two lists of indices of comments, one that have both a cosine similarity of above 0.5 and another a common POS sequence.
Due to the capabilites of my hardware, I needed to process the comments in chunks as we are performing n^2 operation where n is the number of comments we are processing.
You may find that your hardware can process smaller or larger chunks, and if so you can change the chunk size easily. 
The final step is to parse the arrays of indices, which is the function of CC-results.py.
This script will output a list of tuples of similar comments, which can then be easily analysed as a network graph as I did, or through some other method.
