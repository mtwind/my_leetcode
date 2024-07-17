class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) <= 2:
            return nums.index(target) if target in nums else -1
        mid, temp = int(len(nums)/2), nums[0]
        if temp == target:
            return 0
        
        del nums[0]
        nums.insert(mid, temp)
        # determine left and right
        right, left = nums[mid + 1], nums[mid-1]
        
        # choose to go left or right
        if temp < left and temp > right:
            isLeft = target >= temp
        if temp > left and temp > right:
            isLeft = target > temp or target < right      
        if temp < left and temp < right:
            isLeft = target > temp and target < right
        
        num = (self.search(nums[:mid], target) if isLeft else self.search(nums[mid+1:], target)) + 1
        return -1 if num is 0 else (num if isLeft else num + mid)
    
# ultra shorthand
# class Solution:
#     def search(self, nums: List[int], target: int) -> int:
#         if len(nums) <= 2:
#             return nums.index(target) if target in nums else -1
#         mid, temp = int(len(nums)/2), nums[0]
#         if temp == target:
#             return 0
#         del nums[0]
#         nums.insert(mid, temp)
#         right, left = nums[mid + 1], nums[mid-1]
#         isLeft = target >= temp if temp < left and temp > right else (target > temp or target < right if temp > left and temp > right else target > temp and target < right)
#         num = (self.search(nums[:mid], target) if isLeft else self.search(nums[mid+1:], target)) + 1
#         return -1 if num is 0 else (num if isLeft else num + mid)