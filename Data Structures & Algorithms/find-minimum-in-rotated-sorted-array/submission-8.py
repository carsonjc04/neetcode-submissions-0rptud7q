class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        We need to know where the array is rotated, and do binary on the
        smaller side
        EX:
        [4,5,0,1,2,3] = mid = 1. We can check if mid <= right, we know the rotate
        occurs on the other side. So right = mid.
        Other case:
        [4,5,0,1,2,3] mid = 5. check if mid >= right:
        we know the rotation occurs after mid. So move left = mid
        """


        l, r = 0, len(nums) - 1

        while l < r:
            mid = (l + r) // 2
            if nums[mid] <= nums[r]:
                r = mid
            else:
                l = mid + 1
        return nums[l]