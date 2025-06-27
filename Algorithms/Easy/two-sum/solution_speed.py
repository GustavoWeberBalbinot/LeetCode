class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        previous_numb = {}
        for n in range(len(nums)):
            value = target - nums[n]
            if value in previous_numb:
                return [previous_numb[value], n]
            previous_numb[nums[n]] = n
#focus on speed
