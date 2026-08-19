class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        n = len(quiet)

        graph = [[] for _ in range(n)]

        for a, b in richer:
            graph[b].append(a)

        answer = [-1] * n

        def dfs(person):
            if answer[person] != -1:
                return answer[person]

            best = person

            for richer_person in graph[person]:
                candidate = dfs(richer_person)

                if quiet[candidate] < quiet[best]:
                    best = candidate

            answer[person] = best
            return best

        for i in range(n):
            dfs(i)

        return answer