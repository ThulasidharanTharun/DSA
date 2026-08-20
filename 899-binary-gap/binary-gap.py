class Solution:
    def binaryGap(self, n: int) -> int:
        last = -1
        answer = 0
        position = 0
        while n > 0:
            if n & 1:
                if last != -1:
                    answer = max(answer, position - last)
                last = position
            n >>= 1
            position += 1
        return answer