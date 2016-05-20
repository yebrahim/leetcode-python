from collections import Counter,defaultdict
class ValidWordAbbr(object):
    def __init__(self, dictionary):
        self.__d = defaultdict(list)
        for w in dictionary:
            self.__d[w[0]+str(len(w)-2)+w[-1] if len(w) > 2 else w] += [w]

    def isUnique(self, word):
        abbrv = word[0]+str(len(word)-2)+word[-1] if len(word)>2 else word
        return [w for w in self.__d.get(abbrv,[]) if w != word] == []