"""
💡 **Question 1**
Given three integer arrays arr1, arr2 and arr3 **sorted** in **strictly increasing** order, return a sorted array of **only** the integers that appeared in **all** three arrays.

**Example 1:**

Input: arr1 = [1,2,3,4,5], arr2 = [1,2,5,7,9], arr3 = [1,3,4,5,8]

Output: [1,5]

**Explanation:** Only 1 and 5 appeared in the three arrays.

"""
def common_elements(arr1, arr2, arr3):
  

  i = j = k = 0
  result = []
  while i < len(arr1) and j < len(arr2) and k < len(arr3):
    if arr1[i] == arr2[j] == arr3[k]:
      result.append(arr1[i])
      i += 1
      j += 1
      k += 1
    elif arr1[i] < arr2[j]:
      i += 1
    elif arr2[j] < arr3[k]:
      j += 1
    else:
      k += 1
  return result

arr1 = [1,2,3,4,5]
arr2 = [1,2,5,7,9]
arr3 = [1,3,4,5,8]
print(common_elements(arr1, arr2, arr3))

"""
Output:
[Running] python -u "/config/workspace/practices/Assignment 4/ass4Q1.py"
[1, 5]

[Done] exited with code=0 in 0.029 seconds



"""
"""
💡 <aside>
💡 **Question 2**

Given two **0-indexed** integer arrays nums1 and nums2, return *a list* answer *of size* 2 *where:*

- answer[0] *is a list of all **distinct** integers in* nums1 *which are **not** present in* nums2*.*
- answer[1] *is a list of all **distinct** integers in* nums2 *which are **not** present in* nums1.

**Note** that the integers in the lists may be returned in **any** order.

**Example 1:**

**Input:** nums1 = [1,2,3], nums2 = [2,4,6]

**Output:** [[1,3],[4,6]]

**Explanation:**

For nums1, nums1[1] = 2 is present at index 0 of nums2, whereas nums1[0] = 1 and nums1[2] = 3 are not present in nums2. Therefore, answer[0] = [1,3].

For nums2, nums2[0] = 2 is present at index 1 of nums1, whereas nums2[1] = 4 and nums2[2] = 6 are not present in nums2. Therefore, answer[1] = [4,6].

"""
def find_distinct_numbers(nums1, nums2):
  
  seen = set()
  result = [[], []]
  for num in nums1:
    if num not in seen:
      result[0].append(num)
      seen.add(num)
  for num in nums2:
    if num not in seen:
      result[1].append(num)
      seen.add(num)
  return result

nums1 = [1,2,3]
nums2 = [2,4,6]
print(find_distinct_numbers(nums1, nums2))


"""
Output:
[Running] python -u "/config/workspace/practices/Assignment 4/ass4Q2.py"
[[1, 2, 3], [4, 6]]

[Done] exited with code=0 in 0.025 seconds

"""
"""
💡 **Question 1**
Given three integer arrays arr1, arr2 and arr3 **sorted** in **strictly increasing** order, return a sorted array of **only** the integers that appeared in **all** three arrays.

**Example 1:**

Input: arr1 <aside>
💡 **Question 3**
Given a 2D integer array matrix, return *the **transpose** of* matrix.

The **transpose** of a matrix is the matrix flipped over its main diagonal, switching the matrix's row and column indices.

**Example 1:**

Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]

Output: [[1,4,7],[2,5,8],[3,6,9]]

</aside>

"""
def transpose(matrix):
  
  transposed_matrix = []
  for i in range(len(matrix[0])):
    transposed_row = []
    for j in range(len(matrix)):
      transposed_row.append(matrix[j][i])
    transposed_matrix.append(transposed_row)
  return transposed_matrix

matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(transpose(matrix))

"""
Output:
[Running] python -u "/config/workspace/practices/Assignment 4/ass4Q3.py"
[[1, 4, 7], [2, 5, 8], [3, 6, 9]]

[Done] exited with code=0 in 0.025 seconds

"""
"""
💡 <aside>
💡 **Question 4**
Given an integer array nums of 2n integers, group these integers into n pairs (a1, b1), (a2, b2), ..., (an, bn) such that the sum of min(ai, bi) for all i is **maximized**. Return *the maximized sum*.

**Example 1:**

Input: nums = [1,4,3,2]

Output: 4

**Explanation:** All possible pairings (ignoring the ordering of elements) are:

1. (1, 4), (2, 3) -> min(1, 4) + min(2, 3) = 1 + 2 = 3

2. (1, 3), (2, 4) -> min(1, 3) + min(2, 4) = 1 + 2 = 3

3. (1, 2), (3, 4) -> min(1, 2) + min(3, 4) = 1 + 3 = 4

So the maximum possible sum is 4.


"""
def max_pair_sum(nums):
  
  nums.sort()
  max_sum = 0
  for i in range(len(nums) // 2):
    max_sum += min(nums[2 * i], nums[2 * i + 1])
  return max_sum

nums = [1,4,3,2]
print(max_pair_sum(nums))


"""
Output:
[Running] python -u "/config/workspace/practices/Assignment 4/ass4Q4.py"
4

[Done] exited with code=0 in 0.026 seconds




"""
"""
💡 <aside>
💡 **Question 5**
You have n coins and you want to build a staircase with these coins. The staircase consists of k rows where the ith row has exactly i coins. The last row of the staircase **may be** incomplete.

Given the integer n, return *the number of **complete rows** of the staircase you will build*.

**Example 1:**

**Input:** n = 5

**Output:** 2

**Explanation:** Because the 3rd row is incomplete, we return 2.

"""
def staircase_rows(n):
  
  rows = 0
  current_row_coins = 1
  while current_row_coins <= n:
    rows += 1
    current_row_coins += 1
  return rows

n = 5
print(staircase_rows(n))


"""
Output:
[Running] python -u "/config/workspace/practices/Assignment 4/ass4Q5.py"
5

[Done] exited with code=0 in 0.025 seconds


"""
"""
💡 <aside>
💡 **Question 6**
Given an integer array nums sorted in **non-decreasing** order, return *an array of **the squares of each number** sorted in non-decreasing order*.

**Example 1:**

Input: nums = [-4,-1,0,3,10]

Output: [0,1,9,16,100]

**Explanation:** After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100]

</aside>

"""
def sorted_squares(nums):
  

  squares = []
  for num in nums:
    squares.append(num * num)
  squares.sort()
  return squares
nums = [-4,-1,0,3,10]
print(sorted_squares(nums))

"""
Output:
[Running] python -u "/config/workspace/practices/Assignment 4/ass4Q6.py"
[0, 1, 9, 16, 100]

[Done] exited with code=0 in 0.025 seconds



"""
"""
💡 <aside>
💡 **Question 7**
You are given an m x n matrix M initialized with all 0's and an array of operations ops, where ops[i] = [ai, bi] means M[x][y] should be incremented by one for all 0 <= x < ai and 0 <= y < bi.

Count and return *the number of maximum integers in the matrix after performing all the operations*

**Example 1:**

**Input:** m = 3, n = 3, ops = [[2,2],[3,3]]

**Output:** 4

**Explanation:** The maximum integer in M is 2, and there are four of it in M. So return 4.

"""
def max_integers(m, n, ops):
  

  M = [[0 for _ in range(n)] for _ in range(m)]
  max_integer = 0
  count = 0
  for ai, bi in ops:
    for i in range(ai):
      for j in range(bi):
        M[i][j] += 1
        if M[i][j] > max_integer:
          max_integer = M[i][j]
        elif M[i][j] == max_integer:
          count += 1
  return count
m = 3
n = 3
ops = [[2,2],[3,3]]
print(max_integers(m, n, ops))


"""
Output:
[Running] python -u "/config/workspace/practices/Assignment 4/ass4Q7.py"
6

[Done] exited with code=0 in 0.025 seconds


"""
"""
💡 <aside>
💡 **Question 8**

Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].

*Return the array in the form* [x1,y1,x2,y2,...,xn,yn].

**Example 1:**

**Input:** nums = [2,5,1,3,4,7], n = 3

**Output:** [2,3,5,4,1,7]

**Explanation:** Since x1=2, x2=5, x3=1, y1=3, y2=4, y3=7 then the answer is [2,3,5,4,1,7].

</aside>

"""
def rearrange(nums, n):
  
  rearranged_nums = []
  for i in range(n):
    rearranged_nums.append(nums[i])
    rearranged_nums.append(nums[i + n])
  return rearranged_nums
nums = [2,5,1,3,4,7]
n = 3
print(rearrange(nums, n))


"""
Output:
[Running] python -u "/config/workspace/practices/Assignment 4/ass4Q1.py"
[1, 5]

[Done] exited with code=0 in 0.029 seconds

"""