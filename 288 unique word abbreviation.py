class ValidWordAbbr(object):
    def __init__(self, dictionary):
        """
        initialize your data structure here.
        :type dictionary: List[str]
        """
        # "" is a word, dict could have dup words
        self.mp={}
        for word in dictionary:
            if len(word)<=2: abbr=word
            else: abbr=word[0]+str(len(word)-2)+word[-1]
            if abbr not in self.mp: self.mp[abbr]=set([word])
            else: self.mp[abbr].add(word)

    def isUnique(self, word):
        """
        check if a word is unique.
        :type word: str
        :rtype: bool
        """
        # input could be in or out of dict
        # if in dict, could still be unique
        if len(word)<=2: abbr=word
        else: abbr=word[0]+str(len(word)-2)+word[-1]
        if abbr not in self.mp or self.mp[abbr]==set([word]): return True
        else: return False
        
a=ValidWordAbbr([ "deer", "door", "cake", "card" ])
print a.isUnique("dear") # false
print a.isUnique("cart") # true
print a.isUnique("cane") # false
print a.isUnique("make") # true

a=ValidWordAbbr(["hello"])
print a.isUnique("hello") #True

a=ValidWordAbbr(["a","a"])
print a.isUnique("a") #True