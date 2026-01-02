# https://leetcode.com/problems/n-repeated-element-in-size-2n-array/description/?envType=daily-question&envId=2026-01-02


def repeatedNTimes(nums):
        freq_dict = {}
        for num in nums:
            if num in freq_dict:
                return num
            else:
                freq_dict[num] = 1

print(repeatedNTimes([1,2,3,3]))