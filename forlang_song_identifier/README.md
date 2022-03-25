# A tool for identifying the language in which the lyrics of a given song is sung
The checklang.py will query https://www.azlyrics.com and https://www.lyrics.com in order to find in what language a given song is sung. 
The data supplied to this script is the charts data produced by the [acharts scraper](https://github.com/Ursidaeic/ForeignLang-Music/tree/main/acharts). 
The reason multiple sites are queried is in order to reduce the strain on the resources of any one site, as outlined in [James Densmore's](https://towardsdatascience.com/ethics-in-web-scraping-b96b18136f01) guide to ethical web scraping.  
In order that checklang.py functions efficiently, we need to first prep the data created by the [acharts scraper](https://github.com/Ursidaeic/ForeignLang-Music/tree/main/acharts).
This script will parse the data remove duplicate songs, which it will then save to a file named unique.json.
The reason I have elected to separate this function out from the main folder is so users can have more control over the project structure should they wish to replicate it.

This script makes use of the PyCLD2 package for language detection as I found it most accurate. 
Unfortunately I ran into issues install it from pip, and consequently needed to manually download the binary, which can be found [here](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pycld2)
