# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
#         # create an array of 1s
#         # each number will always be updated 
#         result = [False] * len(nums)
#         stack = [1]

#         for i in range(len(nums)):
#             val = stack[-1] * nums[i]
#             stack.append(val)
#         # print(stack)
#         stack.pop()

#         result[-1] = stack.pop()
#         # print(result)
#         # print(stack)
#         temp = nums[-1]
#         for i in range(len(nums) - 2, 0, -1):
#             result[i] = temp * stack.pop()
#             temp = temp * nums[i]
#             # print(f"i: {i}")
#             # print(f"    temp: {temp}")
#             # print(f"    stack: {stack}")
#             # print(f"    result: {result}")
#         result[0] = temp
#         return result


# solution 2
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # create an array of 1s
        # each number will always be updated 
        result = [1]

        for i in range(len(nums) - 1):
            val = result[-1] * nums[i]
            result.append(val)
        print(result)


        temp = nums[-1]
        for i in range(len(nums) - 2, 0, -1):
            result[i] = temp * result[i]
            temp = temp * nums[i]
        result[0] = temp
        return result
        
    
