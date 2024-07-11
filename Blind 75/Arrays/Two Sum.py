class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # loop through the array and with each num find the indexOf target
        for i in range(len(nums)):
            num = target - nums[i]
            if num in nums[i:]:
                return [i, nums.indexOf(num)]