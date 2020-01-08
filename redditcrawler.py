import praw
import os

reddit = praw.Reddit(client_id='d9IVTFu5zmWPSw',
                     client_secret='AZSeKb3SGVE2B8JrJ70eJsg12X4',
                     user_agent='Scrapper',
                     username='Elfinlox',
                     password='runiteoreno234')

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

generateTextChunk('')