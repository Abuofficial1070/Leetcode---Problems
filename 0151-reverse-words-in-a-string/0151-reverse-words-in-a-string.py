class Solution:
    def reverseWords(self, s):
        words = []
        word = []

        for ch in s:
            if ch != " ":
                word.append(ch)
            else:
                if word:
                    words.append("".join(word))
                    word = []

        if word:
            words.append("".join(word))

        words.reverse()

        return " ".join(words)