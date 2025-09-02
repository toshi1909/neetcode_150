from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = {value: index for index, value in enumerate(nums)}
        # num_dict = {value: index for index, value in enumerate(x)}
        for i, value in enumerate(nums):
            remain = target - nums[i]
            if (remain in num_dict) and (i!=num_dict[remain]):
                return [i, num_dict[remain]]
        else:
            return None

    def twoSum2(self, nums: List[int], target: int) -> List[int]:
        num_dict = {}
        for i, value in enumerate(nums):
            remain = target - nums[i]
            if (remain in num_dict) and (i != num_dict[remain]):
                return [num_dict[remain], i]
            else:
                num_dict[nums[i]] = i
        else:
            return None

def main():
    sol = Solution()
    s = [1,2,3,4,1]
    t = 7
    print(sol.twoSum(s,t))

if __name__ == "__main__":
    main()