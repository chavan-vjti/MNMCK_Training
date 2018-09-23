import nltk
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
df_messages = pd.read_csv("SMSSpamCollection", sep='\t', names=['label', 'message'])
messages = [line.rstrip() for line in open("SMSSpamCollection")]
# print(messages[3])
# for index, i in enumerate(messages[:10]):
#     index +=1
#     print("%d. %s" %(index, i))
df_messages['length'] = df_messages['message'].apply(len)
# %matplotlib inline
# print(df_messages.describe())
print(df_messages['length'].plot.hist(bins=40))
