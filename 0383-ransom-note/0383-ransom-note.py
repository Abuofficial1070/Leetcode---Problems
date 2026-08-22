class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        rd={}
        for i in magazine:
            if i in rd:
                rd[i]+=1
            else:
                rd[i]=1
        for ch in ransomNote:
            if ch not in rd or rd[ch]==0:
               return False
            rd[ch]-=1      
        return True

        