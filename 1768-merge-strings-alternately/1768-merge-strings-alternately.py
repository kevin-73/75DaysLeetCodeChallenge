class Solution:
    def mergeAlternately(self, word1, word2):
        res = []
        for a, b in zip(word1, word2):
            res.append(a)
            res.append(b)
        return "".join(res) + word1[len(word2):] + word2[len(word1):]