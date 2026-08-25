class Solution:
    def superpalindromesInRange(self, left: str, right: str) -> int:
        L, R = int(left), int(right)
        limit = int(R ** 0.5) + 1
        count = 0

        for i in range(1, 100000):
            s = str(i)
            root = int(s + s[-2::-1])

            if root > limit:
                break

            square = root * root

            if L <= square <= R and str(square) == str(square)[::-1]:
                count += 1

        for i in range(1, 100000):
            s = str(i)
            root = int(s + s[::-1])

            if root > limit:
                break

            square = root * root

            if L <= square <= R and str(square) == str(square)[::-1]:
                count += 1

        return count