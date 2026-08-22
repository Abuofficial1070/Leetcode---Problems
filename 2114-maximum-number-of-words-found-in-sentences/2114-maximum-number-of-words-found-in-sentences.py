class Solution:
    def mostWordsFound(self, sentences):
        word=0
        for i in sentences:
            a =i.split()
            count = len(a)
            
            if count > word:
                word = count
                
        return word