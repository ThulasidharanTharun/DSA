class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()

        indexed_nums2 = sorted(
            [(nums2[i], i) for i in range(len(nums2))]
        )

        result = [0] * len(nums1)

        left = 0
        right = len(nums1) - 1

        for num in nums1:
            if num > indexed_nums2[left][0]:
                result[indexed_nums2[left][1]] = num
                left += 1
            else:
                result[indexed_nums2[right][1]] = num
                right -= 1

        return result