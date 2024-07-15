import sys
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # iterate through, each time you hit a negative decide if to reest or not
        if len(nums) == 1:
            return nums[0]
        max, sum = nums[0], nums[0]
        for i in range(len(nums)):
            if nums[i] >= 0:
                sum = 0 if sum < 0 else sum
                sum += nums[i]
            else:
                if nums[i] + sum > 0:
                    sum += nums[i] 
                else:
                    sum = nums[i]
            if sum > max:
                max = sum
        return max

# short solution
# import sys
# class Solution:
#     def maxSubArray(self, nums: List[int]) -> int:
#         # iterate through, each time you hit a negative decide if to reest or not
#         if len(nums) == 1:
#             return nums[0]
#         max, sum = -sys.maxsize - 1, -sys.maxsize - 1
#         for i in range(len(nums)):
#             sum += -sum + nums[i] if sum < 0 else nums[i] if nums[i] > 0 else nums[i] if nums[i] + sum > 0 else -sum + nums[i]
#             max = sum if sum > max else max
#         return max