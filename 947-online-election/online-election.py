        
from typing import List
from bisect import bisect_right
from collections import defaultdict

class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.times = times
        self.leaders = []

        count = defaultdict(int)
        leader = -1
        max_votes = 0

        for person in persons:
            count[person] += 1

            if count[person] >= max_votes:
                leader = person
                max_votes = count[person]

            self.leaders.append(leader)

    def q(self, t: int) -> int:
        index = bisect_right(self.times, t) - 1
        return self.leaders[index]

# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)