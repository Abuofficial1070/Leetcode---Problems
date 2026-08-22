class Solution(object):
    def uniqueMorseRepresentations(self, words):
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---",
            "-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-",
            "..-","...-",".--","-..-","-.--","--.."]
        
        count = set()
        
        for i in words:
            code = ""
            for ch in i:
                code += morse[ord(ch) - ord('a')]
            count.add(code)
        
        return len(count)
        