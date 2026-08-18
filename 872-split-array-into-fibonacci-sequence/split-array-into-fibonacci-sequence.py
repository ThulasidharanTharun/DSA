class Solution:
    def splitIntoFibonacci(self, num: str) -> List[int]:
        result = []
        n = len(num)

        def backtrack(index):
            if index == n:
                return len(result) >= 3

            for end in range(index + 1, n + 1):

                if num[index] == '0' and end > index + 1:
                    break

                value = int(num[index:end])

                if value >= 2**31:
                    break

                if len(result) >= 2:
                    expected = result[-1] + result[-2]

                    if value < expected:
                        continue

                    if value > expected:
                        break

                result.append(value)

                if backtrack(end):
                    return True

                result.pop()

            return False

        if backtrack(0):
            return result

        return []