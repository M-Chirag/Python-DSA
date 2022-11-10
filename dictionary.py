# print the key/value pair of a dictionary sorted on value
def printSortedDictionary(D):
    # D.items() returns k,v tuples (k,v), sorted takes a lambda and sorts by values x[1]
    DS = sorted(D.items(), key=lambda x: x[1])
    for k in DS:
        print(k)

# strip word of punctuation and convert to all lower-case


def stripWord(w):
    w = w.replace(".", "")
    w = w.replace(",", "")
    w = w.replace(";", "")
    w = w.replace(":", "")
    w = w.replace("'", "")
    w = w.replace("&", "")
    w = w.replace("\n", "")
    w = w.lower()
    return(w)


wordDict = {}
with open('DOI.txt', 'r') as file:

    # reading each line
    for line in file:

        # reading each word
        for word in line.split():

            # processing the words
            sw = stripWord(word)

            if(len(sw) > 0):

                if sw in wordDict:
                    wordDict[sw] += 1
                else:
                    wordDict[sw] = 1

printSortedDictionary(wordDict)
