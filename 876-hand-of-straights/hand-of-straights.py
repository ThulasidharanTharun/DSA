class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        count = {}

        for card in hand:
            count[card] = count.get(card, 0) + 1

        for card in sorted(count):
            if count[card] > 0:
                needed = count[card]

                for x in range(card, card + groupSize):
                    if count.get(x, 0) < needed:
                        return False

                    count[x] -= needed

        return True