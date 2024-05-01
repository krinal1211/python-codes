class Solution(object):
    def reversePrefix(self, word, ch):
        index = -1
        for i, c in enumerate(word):
            if c == ch:
                index = i
                break
        if index == -1:
            return word
        else:
            return word[:index+1][::-1] + word[index+1:]  
