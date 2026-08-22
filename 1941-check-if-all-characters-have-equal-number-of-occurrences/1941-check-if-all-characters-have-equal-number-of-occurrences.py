class Solution(object):
    def areOccurrencesEqual(self, s):
        fr={}
        for i  in s:
            if i in fr:
                fr[i]+=1
            else:
                fr[i]=1
            values=list(fr.values())       
        for i in values:
            if i !=values[0]:
                return False
        return True   
        