"""
Question 1
Given an integer array nums of length n and an integer target, find three integers
in nums such that the sum is closest to the target.
Return the sum of the three integers.

You may assume that each input would have exactly one solution.

Example 1:
Input: nums = [-1,2,1,-4], target = 1
Output: 2

Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
"""


def three_sum_closest(nums, target):

  nums.sort()
  closest_sum = float("inf")
  for i in range(len(nums)):
    left = i + 1
    right = len(nums) - 1
    while left < right:
      sum = nums[i] + nums[left] + nums[right]
      if abs(sum - target) < abs(closest_sum - target):
        closest_sum = sum
      if sum < target:
        left += 1
      elif sum > target:
        right -= 1
      else:
        return sum
  return closest_sum
nums = [-1,2,1,-4]
target = 1
print(three_sum_closest(nums, target))

"""
Output:
[Running] python -u "/config/workspace/practices/Assignment 3/ass3Q1.py"
2
[Done] exited with code=0 in 0.024 seconds
"""
"""
Question 2
Given an array nums of n integers, return an array of all the unique quadruplets
[nums[a], nums[b], nums[c], nums[d]] such that:
           ● 0 <= a, b, c, d < n
           ● a, b, c, and d are distinct.
           ● nums[a] + nums[b] + nums[c] + nums[d] == target

You may return the answer in any order.

Example 1:
Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
"""


def four_sum(nums, target):
 
  quadruplets = []
  nums.sort()
  for i in range(len(nums)):
    if i > 0 and nums[i] == nums[i - 1]:
      continue
    for j in range(i + 1, len(nums)):
      if j > i + 1 and nums[j] == nums[j - 1]:
        continue
      left = j + 1
      right = len(nums) - 1
      while left < right:
        sum = nums[i] + nums[j] + nums[left] + nums[right]
        if sum == target:
          quadruplets.append([nums[i], nums[j], nums[left], nums[right]])
          left += 1
          right -= 1
        elif sum < target:
          left += 1
        else:
          right -= 1

  return quadruplets
nums = [1,0,-1,0,-2,2]
target = 0
print(four_sum(nums, target))

"""
Output:
[Running] python -u "/config/workspace/practices/Assignment 3/ass3Q2.py"
[[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]

[Done] exited with code=0 in 0.039 seconds
"""
"""

💡 **Question 3**
A permutation of an array of integers is an arrangement of its members into a
sequence or linear order.

For example, for arr = [1,2,3], the following are all the permutations of arr:
[1,2,3], [1,3,2], [2, 1, 3], [2, 3, 1], [3,1,2], [3,2,1].

The next permutation of an array of integers is the next lexicographically greater
permutation of its integer. More formally, if all the permutations of the array are
sorted in one container according to their lexicographical order, then the next
permutation of that array is the permutation that follows it in the sorted container.

If such an arrangement is not possible, the array must be rearranged as the
lowest possible order (i.e., sorted in ascending order).

● For example, the next permutation of arr = [1,2,3] is [1,3,2].
● Similarly, the next permutation of arr = [2,3,1] is [3,1,2].
● While the next permutation of arr = [3,2,1] is [1,2,3] because [3,2,1] does not
have a lexicographical larger rearrangement.

Given an array of integers nums, find the next permutation of nums.
The replacement must be in place and use only constant extra memory.

**Example 1:**
Input: nums = [1,2,3]
Output: [1,3,2]


"""

def next_permutation(nums):
  
  i = len(nums) - 2
  while i >= 0 and nums[i] >= nums[i + 1]:
    i -= 1
  if i < 0:
    nums.reverse()
    return nums
  j = len(nums) - 1
  while j > i and nums[j] <= nums[i]:
    j -= 1
  nums[i], nums[j] = nums[j], nums[i]
  nums[i + 1:] = nums[i + 1:][::-1]
  return nums
nums = [1,2,3]
print(next_permutation(nums))


"""
Output:
[Running] python -u "/config/workspace/practices/Assignment 3/ass3Q3.py"
[1, 3, 2]
[Done] exited with code=0 in 0.024 seconds
"""
"""
Question 4
Given a sorted array of distinct integers and a target value, return the index if the
target is found. If not, return the index where it would be if it were inserted in
order.

You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [1,3,5,6], target = 5
Output: 2
"""


def search_insert(nums, target):
 
  low = 0
  high = len(nums) - 1
  while low <= high:
    mid = (low + high) // 2
    if nums[mid] == target:
      return mid
    elif nums[mid] < target:
      low = mid + 1
    else:
      high = mid - 1
  return low
nums = [1,3,5,6]
target = 5
print(search_insert(nums, target))

"""
Output:
[Running] python -u "/config/workspace/practices/Assignment 3/ass3Q4.py"
2
[Done] exited with code=0 in 0.024 seconds
"""
"""

💡 **Question 5**
You are given a large integer represented as an integer array digits, where each
digits[i] is the ith digit of the integer. The digits are ordered from most significant
to least significant in left-to-right order. The large integer does not contain any
leading 0's.

Increment the large integer by one and return the resulting array of digits.

**Example 1:**
Input: digits = [1,2,3]
Output: [1,2,4]

**Explanation:** The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].


"""


def increment_integer(digits):
 
  carry = 1
  for i in range(len(digits) - 1, -1, -1):
    if digits[i] + carry == 10:
      digits[i] = 0
      carry = 1
    else:
      digits[i] += carry
      carry = 0
  if carry == 1:
    digits.insert(0, 1)
  return digits
digits = [1,2,3]
print(increment_integer(digits))

"""
Output:
[Running] python -u "/config/workspace/practices/Assignment 3/ass3Q5.py"
[1, 2, 4]

[Done] exited with code=0 in 0.031 seconds

"""
"""
Question 6
Given a non-empty array of integers nums, every element appears twice except
for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only
constant extra space.

Example 1:
Input: nums = [2,2,1]
Output: 1
"""


def single_number(nums):
  
  result = 0
  for num in nums:
    result ^= num
  return result
nums = [2,2,1]
print(single_number(nums))


"""
Output:
[Running] python -u "/config/workspace/practices/Assignment 3/ass3Q6.py"
1

[Done] exited with code=0 in 0.025 seconds

"""
"""
Question 7
You are given an inclusive range [lower, upper] and a sorted unique integer array
nums, where all elements are within the inclusive range.

A number x is considered missing if x is in the range [lower, upper] and x is not in
nums.

Return the shortest sorted list of ranges that exactly covers all the missing
numbers. That is, no element of nums is included in any of the ranges, and each
missing number is covered by one of the ranges.

Example 1:
Input: nums = [0,1,3,50,75], lower = 0, upper = 99
Output: [[2,2],[4,49],[51,74],[76,99]]

Explanation: The ranges are:
[2,2]
[4,49]
[51,74]
[76,99]
"""

def find_missing_ranges(nums, lower, upper):
  

  ranges = []
  current_range = [lower, lower]
  for num in nums:
    if num < current_range[1]:
      current_range[1] = num
    elif current_range[1] < num + 1:
      ranges.append(current_range)
      current_range = [num + 1, num + 1]
  if current_range[0] != upper:
    ranges.append(current_range)
  return ranges


nums = [0,1,3,50,75]
lower = 0
upper = 99
print(find_missing_ranges(nums, lower, upper))


"""
Output:
[Running] python -u "/config/workspace/practices/Assignment 3/ass3Q7.py"
[[0, 0], [1, 1], [2, 2], [4, 4], [51, 51], [76, 76]]

[Done] exited with code=0 in 0.025 seconds

"""
"""
Question 8
Given an array of meeting time intervals where intervals[i] = [starti, endi],
determine if a person could attend all meetings.

Example 1:
Input: intervals = [[0,30],[5,10],[15,20]]
Output: false
"""


def can_attend_all_meetings(intervals):
  
  intervals.sort(key=lambda x: x[0])
  for i in range(1, len(intervals)):
    if intervals[i][0] < intervals[i - 1][1]:
      return False
  return True

intervals = [[0,30],[5,10],[15,20]]
print(can_attend_all_meetings(intervals))


"""
Output:
[Running] python -u "/config/workspace/practices/Assignment 3/ass3Q8.py"
False

[Done] exited with code=0 in 0.025 seconds

"""