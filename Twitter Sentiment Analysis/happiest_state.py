from __future__ import division
import sys
import json

#Creating the list to store the 2-letter state codes in United States 
stateList = ["AL", "AK", "AZ", "AR", "CA", 
             "CO", "CT", "DC", "DE", "FL", "GA", 
          "HI", "ID", "IL", "IN", "IA", "KS", 
             "KY", "LA", "ME", "MD", 
          "MA", "MI", "MN", "MS", "MO", "MT", 
             "NE", "NV", "NH", "NJ", 
          "NM", "NY", "NC", "ND", "OH", "OK", 
             "OR", "PA", "RI", "SC", 
          "SD", "TN", "TX", "UT", "VT", 
             "VA", "WA", "WV", "WI", "WY"]

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    
    # Build a dictionary of words' sentiment
    scores = {}
    for line in sent_file:
        term, score = line.split("\t") # tab-delimited
        scores[term] = int(score)

    # Build a list of tweets from the raw data
    tweets = []
    for line in tweet_file:
        data = json.loads(line)

        #filtering the data based on theplace and the non-empty cells
        if 'text' in data.keys() and 'place' in data.keys() and data['place'] != None:
            #Getting the text from the data
            text = data['text'].replace("\n", "").encode('utf-8').strip()
            #Getting the country from the data
            country = data['place']['country_code']
            #Getting the state from the data
            state = data['place']['full_name'].encode('utf-8').strip()[-2::1]

            # Filtering based on the country and checking for the available states in the data
            if country == 'US' and state in stateList:
                tweets.append((text, state))

    
    #The sentiment of a tweet is basically the sum of all the sentiments of the words in the tweet 
    #where the word is from the wordlist else it is assigned a score of zero.
    #
    
    # A sentiment of a tweet is simply the sum of the sentiment of every word
    # in the tweet that appears in the words' sentiment dictionary
    # Afterward, deciding which state is happiest
    stateSentiment = {each:[0, 1] for each in stateList}
    # each is the 2-D list storing 1st value as the sum and second value as a count
    for (tweet, state) in tweets:
    #Assigning the sentiment score to each state
        sentiment = 0.0
        for word in tweet.split():
            if word in scores:
                sentiment += scores[word]
        stateSentiment[state][0] += sentiment
        stateSentiment[state][1] += 1
        
    result = {each:stateSentiment[each][0] / stateSentiment[each][1] for each in stateList}
    #Print the sorted to get the max
    print "Happiest state is"
    print sorted(result, key = result.get)[-1] 
        

if __name__ == '__main__':
    main()