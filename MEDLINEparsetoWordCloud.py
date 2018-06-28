# This script uses the WordCloud algorithm (word_cloud) by A. Mueller to generate a word cloud of the 200 most common words 
# to show up within a Pubmed search list. It will filter for titles and abstracts, and exclude author information and other 
# irrelevant metadata.
#
# 1. Import TEXT file of a list of Pubmed search results in MEDLINE format
# 2. Script will filter out for titles
# 3. (optional) Script will filter out for filler words based on a user-provided list.
# 4. New TEXT file will be passed on to the WordCloud algorithm

def WordCloudGenOnMEDLINE(resultsfile, filteroutwords = []):
    # Reads the Medline export format text file
    medline_results = open(resultsfile).read()
    from wordcloud import WordCloud
    # Generate a word cloud image
    WorkingTitles, TitleString = GetMedlineTitles(medline_results)
    WorkingAbstracts, AbsString = GetMedlineAbstracts(medline_results)
    
    # Filter out the words that are not to be included in the word cloud.
    if len(filteroutwords) != 0:
        TitleString = WordFilter(TitleString, filteroutwords)
        AbsString = WordFilter(AbsString, filteroutwords)
    ArticleHeaderText = TitleString + AbsString
        
    wordcloud = WordCloud(max_font_size=80).generate(ArticleHeaderText)
    WordFrequencyPlot = plt.figure()
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.show()
    WordFrequencyPlot.savefig('Title&AbstractsMap.png')

# Returns journal titles from an input search results list, in the form of a list and a concatenated string. 
# A,B = GetMedlineTitles(X) will return A as a list and B as a concatenated string.
def GetMedlineTitles(MedlineFormatSearchResults):
    # Parses the Medline export into a list that is split based on 
    # metadata headers. The typical divider between metadata type is a 
    # hypthen with a space.
    medline_results_to_list = MedlineFormatSearchResults.split('- ')
    numtitles = MedlineFormatSearchResults.count('TI  - ')
    title_indices = [0 for x in range(numtitles)]
    j = 0

    # Following section loops through the parsed Medline export and grabs the locations of the article titles.
    for i in range(len(medline_results_to_list)):
        if '\nTI' in medline_results_to_list[i]:
            title_indices[j] = i + 1
            j += 1

    # Stores the titles of the individual research articles into a new list.
    titles = [0 for x in range(numtitles)]         
    titles_as_string = ''
    for i in range(numtitles):
        titles[i] = medline_results_to_list[title_indices[i]][:-5]    
        titles[i] = titles[i].replace('\n     ', '')
        titles_as_string += titles[i] + ' '
    return(titles, titles_as_string)

def GetMedlineAbstracts(MedlineFormatSearchResults):
    medline_results_to_list = MedlineFormatSearchResults.split('- ')
    numabstracts = MedlineFormatSearchResults.count('AB  - ')
    abs_indices = [0 for x in range(numabstracts)]
    j = 0

    # Following section loops through the parsed Medline export and grabs the locations of the article titles.
    for i in range(len(medline_results_to_list)):
        if '\nAB' in medline_results_to_list[i]:
            abs_indices[j] = i + 1
            j += 1

    # Stores the titles of the individual research articles into a new list.
    abstracts = [0 for x in range(numabstracts)]         
    abs_as_string = ''
    for i in range(numabstracts):
        abstracts[i] = medline_results_to_list[abs_indices[i]][:-5]    
        abstracts[i] = abstracts[i].replace('\n     ', '')
        abs_as_string += abstracts[i] + ' '
    return(abstracts, abs_as_string)

def WordFilter(Text, FillerWords):
    for i in range(len(FillerWords)):
        Text = Text.replace(FillerWords[i], ' ')
    return Text
