from typing import List

class Solution:
    # time: O(n+m)
    # space: O(1) since we have at most 26 different characters.

    def isAnagram_sol1(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_dict = {}

        for char in s:
            if char not in s_dict:
                s_dict[char] = 1
            else:
                s_dict[char] += 1

        for char in t:
            if char in s_dict:
                if s_dict[char] == 1:
                    del s_dict[char]
                else:
                    s_dict[char] -= 1
            else:
                return False

        return True

    def isAnagram_sol2(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_dict, t_dict = {}, {}

        for i in range(len(s)):
            s_dict[s[i]] = 1 + s_dict.get(s[i], 0)
            t_dict[t[i]] = 1 + t_dict.get(t[i], 0)

        return s_dict == t_dict

def main():
    sol = Solution()
    s = "abra"
    t = "arbd"
    print(sol.isAnagram_sol2(s,t))

if __name__ == "__main__":
    main()