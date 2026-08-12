class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        summ = []
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i]+nums[j]==target:
                    summ.append(i)
                    summ.append(j)
                    return summ
        