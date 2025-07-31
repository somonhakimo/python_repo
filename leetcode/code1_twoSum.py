# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

 

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:

# Input: nums = [3,3], target = 6
# Output: [0,1]

inp1 = input("put a list of integer numbers here: ")
str_nums = inp1.split()
nums = [int(num) for num in str_nums]

target = int(input('put the sum of two numbers that you provided in the list: '))

def twoSum(nums: list[int], target: int) -> list[int]:
    seen = {}
    for index, number in enumerate(nums):
        complement = target - number
        if complement in seen:
            return [seen[complement], index]
        seen[number] = index
result = twoSum(nums, target)
print(result) 


