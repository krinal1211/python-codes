class Solution(object):
    def deckRevealedIncreasing(self, deck):
        deck.sort()
        deck.reverse()
        l=len(deck)
        array=[]
        i=0
        # or
        # deck = deck[::-1]
        if len(deck)==1:
            return deck
        if len(deck)>=2:
            array.append(deck[i+1])
            array.append(deck[i])
            if len(deck)>2:
                for i in range(2,l):
                    last=array.pop()
                    array.insert(0, last)
                    array=[deck[i]]+array
                return array
            return array


        
