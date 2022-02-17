# install textblob

from textblob import TextBlob
y=input("TYPE YOUR SENTENCES")
edu=TextBlob(y)
x=edu.sentiment.polarity
if x<0:
    print("NEGATIVE:(")
elif x==0:
    print("NEUTRAL :}")
elif x>0 and x<=1:
    print("POSITIVE:)")