class Solution:
    def compress(self, chars: list[str]) -> int:
        write = 0
        read = 0
        while read < len(chars):
            count = 0
            char = chars[read]
            while read < len(chars) and chars[read] == char:
                read += 1
                count += 1
            chars[write] = char
            write += 1
            if count > 1:
                for c in str(count):
                    chars[write] = c
                    write += 1
        print(chars)
        return write


sol = Solution()
print(sol.compress(["a", "a", "b", "b", "c", "c", "c"]))
print(sol.compress(["a"]))
print(sol.compress(["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]))
