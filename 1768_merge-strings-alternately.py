class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i: int = 0
        j: int = 0
        merge = ""
        while i < len(word1) or j < len(word2):
            if i < len(word1):
                merge += word1[i]
                i += 1
            if j < len(word2):
                merge += word2[j]
                j += 1
        return merge


sol = Solution()
print(sol.mergeAlternately("abcdef", "pqr"))
