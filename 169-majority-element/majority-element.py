class Solution(object):
    def majorityElement(self, nums):
        a={}
        half=len(nums)/2
        for i in range(len(nums)):
            if nums[i] not in a:
                a[nums[i]]=1
            else:
                a[nums[i]]+=1
        for key,value in a.items():
            if value>half:
                return key
            
        
        