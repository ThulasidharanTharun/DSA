class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        result = list(s)
        total = 0
        for i in range(len(s) - 1, -1, -1):
            total = (total + shifts[i]) % 26
            result[i] = chr(
                (ord(s[i]) - ord('a') + total) % 26 + ord('a')
            )
        return ''.join(result)