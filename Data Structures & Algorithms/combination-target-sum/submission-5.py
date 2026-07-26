class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        """
        We will use a backtracking method, Basically from every position we can
        either include the current value, or exclude. From there we will 
        recursively call our function to once again include or exclude.
        This pattern allows us to try all potential results.

        Approach:
        1. create backtracking helper function that passes index, cur, total
        2. We will use the index to track our number we are on, cur to track
        our subset and total to track whether subset >, < ,or == target
        3. if i >= len(nums) or total >= target, return since we know thats the end of this iteration
        4. if total == target and 
        5. cur.append(nums[i]). backtrack(i + 1,cur, total += nums[i])
        6. cur.pop(), backtrack(i, cur, total)
        7. call backtrack and return res
        """

        res = []

        def backtrack(i, cur, total):
            if i >= len(nums) or total > target:
                return
            if target == total:
                res.append(cur.copy())
                return
            
            cur.append(nums[i])
            backtrack(i, cur, total + nums[i])
            cur.pop()
            backtrack(i + 1, cur, total)
        
        backtrack(0, [], 0)
        return res