# MedlineResultsMaps
My ongoing personal project to derive quantitative results and data visualization from a set of Pubmed/Medline results.

# MEDLINEparsetoWordCloud.py
This code will take in a standard MEDLINE format export of Pubmed results and create a word cloud of the 200 most common words appearing in the titles and abstracts. The titles and abstracts can be also filtered to remove filler words such as 'background', 'results', etc., but these are user-defined rather than being an automated 'smart' system. I am working on a better filter based on the NLTK toolkit.
This code has dependencies on A. Mueller's Wordcloud function - https://github.com/amueller/word_cloud , which in has a number of other dependencies itself.
