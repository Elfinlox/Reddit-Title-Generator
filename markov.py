import random
import pandas as pd

def generateWords(subreddit):
    with open(subreddit + '.txt', "r") as txt:
        wordlist = txt.read().split()
    return wordlist

def markov(wordlist):
    col = pd.unique(wordlist)
    data = [[0 for word in col] for word in col]
    df = pd.DataFrame(data, index = col, columns = col)
    for i in range(0, len(wordlist) - 1):
        df.loc[wordlist[i], wordlist[i+1]] += 1
    markovchain = df.div(df.sum(axis = 1), axis = 0)
    return markovchain

def generateChain(subreddit):
    markov(generateWords(subreddit)).to_pickle(subreddit)

generateChain('worldnews')