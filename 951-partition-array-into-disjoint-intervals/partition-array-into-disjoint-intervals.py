
class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        left_max = nums[0]
        current_max = nums[0]
        partition = 1

        for i in range(1, len(nums)):
            current_max = max(current_max, nums[i])

            if nums[i] < left_max:
                partition = i + 1
                left_max = current_max

        return partition