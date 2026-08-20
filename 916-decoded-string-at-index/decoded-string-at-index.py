class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        size = 0

        for ch in s:
            if ch.isdigit():
                size *= int(ch)
            else:
                size += 1

        for ch in reversed(s):
            if ch.isdigit():
                size //= int(ch)
                k %= size
            else:
                if k == 0 or k == size:
                    return ch
                size -= 1