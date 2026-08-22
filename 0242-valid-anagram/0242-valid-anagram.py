class Solution(object):
    def isAnagram(self, s, t):
        sd={}
        td={}
        for ch in s:
            if ch in sd:
                sd[ch]+=1
            else:
                sd[ch]=1
        for ch in t:
            if ch in td:
                td[ch]+=1
            else:
                td[ch]=1
        if sd==td:
            return True
        else:
            return False
        