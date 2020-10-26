import pandas as pd
import seaborn as sns
import numpy as np

import string

noThanks = string.punctuation
noThanks += "1234567890"

def cleanText(someText):
    someText = someText.replace('\n',' ') # new lines
    temp = ""
    for i in someText:
        if i in noThanks:
            temp += " "
        else:
            temp += i
            
    return temp

english5 = open("fiveArticles.txt","r",encoding="UTF-8")

englishStr = ""

for line in english5:
    englishStr += line


from nltk.corpus import stopwords

swEnglish = stopwords.words('english')

englishStrClean = cleanText(englishStr).lower().split()

englishStrCleaner = [word for word in englishStrClean if word not in swEnglish]

englishStrCleaner[:10]

corpusDict = {}

for i in englishStrCleaner:
    if i in corpusDict:
        corpusDict[i] +=1
    else:
        corpusDict[i] = 1


df = pd.DataFrame(data=[[i, corpusDict[i]] for i in corpusDict ], columns=["word", "freq"])


df.sort_values(by="freq",ascending=False, inplace=True)
df.reset_index(drop=True, inplace=True)


df["ind"] = np.arange(0,1981)



g = sns.barplot(data=df, y="freq", x="ind")

for ind, label in enumerate(g.get_xticklabels()):
    if ind % 500 == 0:  # x ticks
        label.set_visible(True)
    else:
        label.set_visible(False)

#g.xlabel("someWordIndex")
g.set(ylim=(0, 45))
g.set(xlim=(0, 2000))


