class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        maxNum = nums[0]
        resets = [0]
        for i in range(len(nums)):
            sub = 0
            if nums[i] < 0:
                resets.append(0)
                sub = 1
            # print(f"i:{i}")
            # print(f"    {resets}")
            for j in range(len(resets) - sub):
                resets[j] = resets[j] * nums[i] if resets[j] is not 0 else nums[i]
                if resets[j] > maxNum:
                    maxNum = resets[j]
            # print(f"    {resets}")
        # print(resets)
        return maxNum