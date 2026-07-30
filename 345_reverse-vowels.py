class Solution:
    def reverseVowels(self, s: str) -> str:
        j = len(s) - 1
        word = list(s)
        i = 0
        vowels = "aeiouAEIOU"
        while i < j:
            while i < j and vowels.find(word[i]) == -1:
                i += 1
            while i < j and vowels.find(word[j]) == -1:
                j -= 1
            word[i], word[j] = word[j], word[i]
            i += 1
            j -= 1
        return "".join(word)


sol = Solution()
print(sol.reverseVowels("IceCreAm"))
