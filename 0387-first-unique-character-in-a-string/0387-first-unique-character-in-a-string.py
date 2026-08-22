class Solution(object):
    def firstUniqChar(self, s):
        freq={}
        for ch in s:
            if ch in freq:
                freq[ch]+=1
            else:
                freq[ch]=1
        for ch,j in enumerate(s):
            if freq[j]==1:
                return ch
        
        return -1   
        