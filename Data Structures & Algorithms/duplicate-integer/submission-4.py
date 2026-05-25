class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dict = {}
        for i in nums:
            if i in dict:
                dict[i] += 1
                if dict[i] == 2:
                    return True
            else:
                dict[i] = 1
        return False