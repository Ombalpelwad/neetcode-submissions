class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: 
            return 0
            
        nums.sort()
        max_count = 1
        count = 1
        for i in range(len(nums)-1):
            if nums[i+1] == nums[i]:
                continue
            if nums[i+1] == nums[i] + 1:
                count = count + 1
            else:
                count = 1
            if count > max_count:
                max_count = count
        return max_count