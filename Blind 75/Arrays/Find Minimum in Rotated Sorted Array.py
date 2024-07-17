class Solution:
    def findMin(self, nums: List[int]) -> int:
        # [4,5,6,7,8,9,0,1,2]
        # put 4 in middle [5,6,7,8,4,9,0,1,2] -> [4,9,0,1,2]
        # if both adjacent nums are larger, search right side
        # put 4 in middle [9,0,4,1,2] -> [9,0,4]
        # if both are smaller, search left side
        # put 9 in middle [0,9,4] -> [0,9] -> 0
        
        # [4,5,6,7,0,1,2]
        # put 4 in middle [5,6,7,4,0,1,2] -> [4,0,1] result is adjacent to right
        return self.search(nums)
    
    def search(self, nums: List[int]) -> int:
        # base case
        if len(nums) <= 2:
            return min(nums)
        
        # insert front into middle
        mid = len(nums) / 2
        mid = int(mid)
        temp = nums[0]
        del nums[0]
        nums.insert(mid, temp)
        
        minNum = temp
        # determine left and right
        right = nums[mid + 1]
        left = nums[mid-1]
        # both larger, search right
        if (right > temp and left > temp):
            minNum = self.search(nums[mid:])
        elif (right < temp and left < temp):
            minNum = self.search(nums[:mid+1])
        else:
            minNum = right
        return minNum
        
