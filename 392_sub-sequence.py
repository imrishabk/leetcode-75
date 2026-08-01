class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s == "":
            return True
        if len(s) > len(t):
            return False
        i = 0
        j = 0
        while j < len(t):
            if i < len(s) and s[i] == t[j]:
                i += 1
            j += 1
            if i == len(s):
                return True
        print(i, j)
        return False


sol = Solution()
print(sol.isSubsequence("abc", "ahbgdc"))
print(sol.isSubsequence("axc", "ahbgdc"))
print(sol.isSubsequence("b", "c"))
