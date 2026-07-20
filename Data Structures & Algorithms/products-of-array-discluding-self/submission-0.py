import math

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        ls = nums.copy()
        for i in range(len(nums)):
            ls.pop(i)
            o = math.prod(ls)
            output.append(o)
            ls = nums.copy()
        return output
        