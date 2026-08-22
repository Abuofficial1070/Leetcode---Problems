class Solution(object):
    def longestPalindrome(self, s):
        fr={}
        for ch in s:
            if ch in fr:
                fr[ch]+=1
            else:
                fr[ch]=1
        length=0
        odd=False
        for ch in fr.values():
            if ch%2==0:
                length+=ch
            else:
                length+=ch-1
                odd=True
        if odd:
            length+=1

        return length

        