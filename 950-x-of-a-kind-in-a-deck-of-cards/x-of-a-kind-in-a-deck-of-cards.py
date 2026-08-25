from typing import List
from collections import Counter
from math import gcd
from functools import reduce

class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        count = Counter(deck)

        common = 0

        for freq in count.values():
            common = gcd(common, freq)

        return common > 1