class Solution(object):
    def thirdMax(self, nums):
        nums.sort()
        a=[]
        for i in range(len(nums)):
            if nums[i] not in a:
                a.append(nums[i])
        
        if len(a)>=3:
            return a[-3]
        else:
            return a[-1]
        