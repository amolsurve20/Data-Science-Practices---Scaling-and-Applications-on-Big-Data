from __future__ import division
import sys
import json
import re

def main():
    tweet_file = open(sys.argv[1])

    #Creating an empty list to store the hashtags
    hashTags = []
    
    #Iterating over every line in the file
    for line in tweet_file:
        data = json.loads(line)
        #Searching for entities keyword in the json
        if "entities" in data.keys():
            #searching for hashtag keyword in the json
            for elem in data["entities"]["hashtags"]:  
                tag = elem["text"]
                hashTags.append(tag.replace("\n", "").encode('utf-8').strip())    

    # Creating an empty dictionary to store the count of the hashtag
    tagCount = {}
    
    #iterating over every tag in the dictionary
    for tag in hashTags:
        #i the tag is already present, increment the tag count
        if tag in tagCount:
            tagCount[tag] += 1.0
        else:
            #if the tag is not present, initialize the count to one
            tagCount[tag] = 1.0
    #Sorting the dictionary to get the top 10 hashtags        
    topTen = sorted(tagCount, key = tagCount.get)[-10::1]
    for tag in topTen[::-1]:
        print tag, tagCount[tag]

if __name__ == '__main__':
    main()