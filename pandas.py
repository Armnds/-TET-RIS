import pandas as pd

a = pd.read_excel("#file") #loading database



#filter
print(a(["speaking_line"] == True)) #only show the data where speaking_line is True

#OPERATIONS: average, minimum words spoken, sum etc.
#sum mean max min

a["word_count".sum]