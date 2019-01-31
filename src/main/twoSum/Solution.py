class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = {}

        for i in range(len(nums)):
            rem = target - nums[i]

            if rem in dic:
                return [dic[rem], i]
            else:
                dic[nums[i]] = i

        return []
