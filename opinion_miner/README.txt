A Support Vecotor Machine trained on YouTube comments to identify comments that contain opinion-sentiment. A pickled trained model is supplied but the scripts used to train said model are as well if you have your own dataset.

In the resources folder there are 3 useful dictionaries for PRSR.py:
1) abbreviations: a list of common abbreviations to be checked against when spell checking strings.
2) NAMES: names of artists whose songs I was downloading as, by the very nature of them being foreign language songs, these names are unlikely to be included in English-language dictionaries
3) contractions: a resource compiled by Github user dipanjanS for expanding out contractions. Some of the code used in PRSR.py is taken directly from their guide to pre-processing text for NLP (source: https://www.kdnuggets.com/2018/08/practitioners-guide-processing-understanding-text-2.html)
