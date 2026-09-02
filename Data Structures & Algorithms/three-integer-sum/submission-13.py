class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        """
        we'll iterate through nums and do a binary search on the remaining window, however we know we cannot use duplicates so when we start our binary search, ensure that first value != i
        """
        nums.sort()
        res = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l, r = i + 1, len(nums) - 1
            
            while l < r:
                cur = nums[i] + nums[r] + nums[l]
                if cur > 0:
                    r -= 1
                elif cur < 0:
                    l += 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
        return res