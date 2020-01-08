import random
import pandas as pd

def sentenceGenerator(markovchain):
    lastword = 's'
    sentence = ['s']
    while lastword != 'e':
        lastword = nextword(lastword, markovchain)
        sentence = sentence + [lastword]
    for i in range(len(sentence)):
        if sentence[i-1] in '.?!':
            sentence[i] = sentence[i][0].upper() + sentence[i][1:]
    quote = ''
    for word in sentence[1:-1]:
        quote = quote + word + ' '
    quote = quote[:-1]
    quote = quote.replace(' .', '.')
    quote = quote.replace(' ?', '?')
    quote = quote.replace(' !', '!')
    quote = quote.replace(' ,', ',')
    quote = quote[0].upper() + quote[1:]
    return quote

def nextword(word, markovchain):
    words = list(markovchain.columns)
    chance = markovchain.loc[word, :]
    return random.choices(words, chance)[0]

def newPost(subreddit):
    markov = pd.read_pickle(subreddit)
    print(sentenceGenerator(markov))

if __name__ == "__main__":
    subreddit = input("Enter subreddit name: ")
    newPost(subreddit)