class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        result = set()
        current = set()

        for num in arr:
            current = {num | x for x in current}
            current.add(num)

            result.update(current)

        return len(result)