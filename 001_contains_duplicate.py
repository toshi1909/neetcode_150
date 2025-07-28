from typing import List

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # time: O(n)
        # space: O(n)
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False


def main():
    nums = [1,2,3,4,1]
    solution = Solution()
    if solution.hasDuplicate(nums):
        print("Correct solution")
    else:
        print("Wrong solution")

# Call the main method
if __name__ == "__main__":
    main()