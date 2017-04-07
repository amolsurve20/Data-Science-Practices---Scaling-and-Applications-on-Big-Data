from __future__ import division
import sys
import json
import re

def main():
    tweet_file = open(sys.argv[1])

    # Build a list of tweets from the raw data
    tweetList = []
    for line in tweet_file:
        data = json.loads(line)
        if 'text' in data.keys():
            tweetList.append(data['text'].replace("\n", "").encode('utf-8'))
    tweetList = filter(bool, tweetList)

    # Evaluate the frequency of every term by the following formula
    # [# of occurrences of the term in all tweets] / [# of occurrences of all terms in all tweets]
    allTerms = {}
    totalTerms = 0
    for tweet in tweetList:
        tweetWords = tweet.split()
        totalTerms += len(tweetWords)
        for word in tweetWords:
            if word not in allTerms:
                allTerms[word] = 1.0 
            else: 
                allTerms[word] += 1.0

    for term in allTerms:
        print term, allTerms[term] / totalTerms

if __name__ == '__main__':
    main()