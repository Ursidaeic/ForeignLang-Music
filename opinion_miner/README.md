# Scripts for filtering comments based off language and content 
There are two tools included in this project. The first is a tool for filtering comments based off the language used in them. This makes use of the PyCLD2 package, which I had trouble installing using pip. To work around this, I installed the package using the binary, which can be found [here](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pycld2). The second is a Support Vector Machine that I used to filter these English-language comments based off whether there was an opinion expressed in them. The tagged training set I used for this has been included in the resources folder, but you may wish to provide your own if you are using a different dataset than my own (all of which can be found [here](https://drive.google.com/drive/folders/1f6OK0lZTwU937JwAzNPQXyRbNwlp8XxZ?usp=sharing). 

If you do wish to use your own corpus of comments, or even recreate this methodology with my own, then simply place the comments you wish to apply these tools to in the comments folder.