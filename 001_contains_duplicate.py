from typing import List

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        num_dict = {}

        for n in nums:
            if n not in num_dict:
                num_dict[n] = None
            else:
                return True
        else:
            return False
