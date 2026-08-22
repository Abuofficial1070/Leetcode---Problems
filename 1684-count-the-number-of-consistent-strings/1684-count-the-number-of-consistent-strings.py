class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        fr=set(allowed)
        count=0
        for word in words:
            flag= True
            for ch in word:
                if ch not in fr:
                    flag = False
                    break
            if flag:
                count+=1
        return count
