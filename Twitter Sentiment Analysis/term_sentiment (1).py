import sys
import json

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    otherWords={}

    # Build a dictionary of words' sentiment
    scores = {}
    for line in sent_file:
        term, score = line.split("\t") 
        # tab-delimited
        scores[term] = int(score)

    # Build a list of tweets from the raw data
    tweets = []
    for line in tweet_file:
        data = json.loads(line)
        if 'text' in data.keys():
            tweets.append(data['text'].encode('utf-8'))

    
    # A sentiment of a tweet = Sum of the sentiment of every word
    # in the tweet that appears in the words' sentiment dictionary
    for tweet in tweets:
        sentiment=0.0
        for word in tweet.split(" "):
            if word in scores:
                sentiment=sentiment+scores[word]
            
        for word in tweet.split(" "):
            if word not in scores:
                if word not in otherWords:
                    #if the word is appearing for the first time, assign the sentiment score of 1 to it
                    otherWords[word]=[sentiment,1]
                else:
                    #else, if the word is already in the newly constructed dictionary, increment the score
                    otherWords[word][0]+=sentiment
                    otherWords[word][1]+=1
    
    result = {term:otherWords[term][0]/otherWords[term][1] for term in otherWords}
    for term in result:
        print term, result[term]

if __name__ == '__main__':
    main()