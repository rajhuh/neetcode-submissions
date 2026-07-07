class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l,r=0,0
        stack=[]
        n=len(nums)
        for l in range(0,n):
            for r in range(l + 1, n):
                if nums[l]+nums[r]==target:
                    stack.append(l)
                    stack.append(r)
                    return stack
        return stack