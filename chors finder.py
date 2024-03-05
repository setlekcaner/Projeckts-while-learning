lyrics = list(map(str, input().split()))
def lyrics_times(lyrics):
    mydict = {}
    for word in lyrics:
        if word in mydict:
            mydict[word] += 1
        else:
            mydict[word] = 1
    return mydict


def most_common(mydict):
    values = mydict.values()
    best = max(values)
    words = []
    for k in mydict:
        if mydict[k] == best:
            words.append(k)
    return (words, best)


print(most_common(lyrics_times(lyrics)))
