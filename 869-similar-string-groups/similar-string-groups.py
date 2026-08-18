class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        def similar(a, b):
            diff = 0
            for i in range(len(a)):
                if a[i] != b[i]:
                    diff += 1

                    if diff > 2:
                        return False

            return diff == 0 or diff == 2
        visited = set()
        groups = 0

        def dfs(i):
            visited.add(i)

            for j in range(len(strs)):
                if j not in visited and similar(strs[i], strs[j]):
                    dfs(j)

        for i in range(len(strs)):
            if i not in visited:
                groups += 1
                dfs(i)

        return groups