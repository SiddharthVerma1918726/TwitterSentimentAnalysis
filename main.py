from tkinter import messagebox
import tkinter as tk
from tkinter import *
from textblob import TextBlob
import sys,tweepy
import matplotlib.pyplot as plt

consumerKey = "D0BrnZTFu7fHoV5aYhDHm2aLj"
consumerSecret = "9YSiAIEG2wLvFk5ooXVMdt9NMEGfSmZwhjq7rex9Pggf2VtPdA"
accessToken = "1505122165079044100-jti9xY0EGYWwmvDfrmxLsn5WNymFct"
accessTokenSecret = "0Cqkg62mDzIWOL6AzrCXjemuV6H5FyVJhjTFtyyCUOzyy"

auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
auth.set_access_token(accessToken, accessTokenSecret)
api = tweepy.API(auth)

window=tk.Tk()
window.geometry("950x483")
bg = PhotoImage(file = "C:/Users/hp/Downloads/twitter5.png")

label1 = Label( window, image = bg)
label1.place(x = 0, y = 0)

window.title("Sentiment Analysis ")
window.config(background="white")


m=tk.Label()
m.grid(column=3,row=0)
X=tk.Label(window,text="Hashtag",font=('Algerian',20),bg= '#18384d',fg='#e3e3e1', pady=5, padx=5)
X.grid(column=3,row=1)
X1=tk.Entry(window,width=50,bd=5)
X1.grid(column=4,row=1)

Y=tk.Label(window,text="No of Tweets",font=('Algerian',20),bg= '#18384d',fg='#e3e3e1', pady=5, padx=5)
Y.grid(column=3,row=2)
Y1=tk.Entry(window,width=50,bd=5)
Y1.grid(column=4,row=2)


def exit():
    window.quit()


def analyse():
    def percentage(part, whole):
        return 100 * float(part) / float(whole)

    searchterm = X1.get()
    if (searchterm == '' or Y1.get() == ''):
        messagebox.showinfo("Warning", "Fill the hashtag field and No_of_tweets should be greater than 0")
    noOfsearch = int(Y1.get())
    if(len(searchterm)>0 and len(Y1.get())>0 ):
        tweets = tweepy.Cursor(api.search_tweets, q=searchterm).items(noOfsearch)

        positive = 0
        negative = 0
        neutral = 0
        polarity = 0

        for tweet in tweets:
            # print(tweet.text)
            analysis = TextBlob(tweet.text)
            polarity += analysis.sentiment.polarity
            if analysis.sentiment.polarity == 0:
                neutral += 1
            elif analysis.sentiment.polarity > 0:
                positive += 1
            else:
                negative += 1

        positive = percentage(positive, noOfsearch)
        negative = percentage(negative, noOfsearch)
        neutral = percentage(neutral, noOfsearch)

        positive = format(positive, '.2f')
        negative = format(negative, '.2f')
        neutral = format(neutral, '.2f')

        label = ['Positive [' + str(positive) + '%]', 'Negative [' + str(negative) + '%]',
                 'Neutral [' + str(neutral) + '%]']
        size = [positive, negative, neutral]
        colors = ['yellow', 'green', 'red']
        patches, texts = plt.pie(size, colors=colors, startangle=45)
        plt.legend(patches, label, loc="best")
        plt.title('Data collected from ' + str(noOfsearch) + ' tweets' + ' on topic ' + searchterm)
        plt.axis('equal')
        plt.tight_layout()
        plt.show()

b3=tk.Button(window,text="Analyse",font=("Argerian",16),bg='#127f9d',fg='#e3e3e1',command=analyse)
b3.grid(column=4,row=4)

b3=tk.Button(window,text="Exit",font=("Argerian",16),bg='#127f9d',fg='#e3e3e1',command=exit)
b3.grid(column=3,row=4)
window.mainloop()


















