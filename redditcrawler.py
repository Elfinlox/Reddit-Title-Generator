import praw
import os
import random
import pandas as pd 
import markov

reddit = praw.Reddit(client_id='',
                     client_secret='',
                     user_agent='',
                     username='',
                     password='')

def generateTextChunk(sub):
    subreddit = reddit.subreddit(sub)
    with open(sub + 'test.txt', "w") as w:
        for submission in subreddit.top('all',limit = 1000):
            try:
                w.write(submission.title + ' e s ')
            except:
            	pass
    with open(sub + 'test.txt', "r") as r, open(sub + '.txt', "w", encoding = "utf-8") as w:
        w.write('s ')
        for char in r.read():
            if char in ".,!?":
                w.write(' ' + char)
            elif char in '''"“”''':
                pass
            else:
                w.write(char.lower())
    os.remove(sub + 'test.txt')

if __name__ == "__main__":
    subreddit = input("Enter subreddit name: ")
    generateTextChunk(subreddit)
    markov.generateChain(subreddit)