from typing import List
from collections import Counter

class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        required = Counter()

        for word in words2:
            count = Counter(word)

            for char in count:
                required[char] = max(required[char], count[char])

        result = []

        for word in words1:
            count = Counter(word)

            if all(count[char] >= required[char] for char in required):
                result.append(word)

        return result