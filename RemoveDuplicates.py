class Solution(object):
    def removeDuplicates(self, nums):
        
        l2=[]
        for i in nums:
            if i not in l2:
                l2.append(i)

        size=len(l2)
        for i in range(0,size):
            nums[i]=l2[i]

        return size  
