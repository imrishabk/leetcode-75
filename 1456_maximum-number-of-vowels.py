class Solutions:
    def maxVowels(self, s: str, k: int) -> int:
        n = len(s)

        vowels = set("aeiou")
        count = sum(1 for c in s[:k] if c in vowels)
        max_count = count

        for i in range(n - k):
            if s[i + k] in vowels:
                count += 1
            if s[i] in vowels:
                count -= 1
            max_count = max(max_count, count)
        return max_count


sol = Solutions()
print(sol.maxVowels("abciiidef"))
