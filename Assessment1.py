""""
💡 **Q1.** Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

**Example:**
Input: nums = [2,7,11,15], target = 9
Output0 [0,1]

**Explanation:** Because nums[0] + nums[1] == 9, we return [0, 1] """

def twoSum(nums, target):
    
    d = {}

    for i, num in enumerate(nums):
        j = target - num
        
        if j in d:
            return [d[j], i]
      
        d[num] = i
    return []

nums = [2, 7, 11, 15]
target = 9
result = twoSum(nums, target)
print(result)  

"""
Output:

[Running] python -u "/config/workspace/practices/ass1Q1.py"
[0, 1]
[Done] exited with code=0 in 0.025 seconds

"""
""""
💡 💡 **Q2.** Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.
Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:
- Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
- Return k.

**Example :**
Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2,_*,_*]

**Explanation:** Your function should return k = 2, with the first two elements of nums being 2. It does not matter what you leave beyond the returned k (hence they are underscores)

 """

def remove(nums, val):
    i = 0
    
    
    for j in range(len(nums)):
       
        if nums[j] != val:
            nums[i] = nums[j]
            i += 1
    
    
    return i


nums = [3, 2, 2, 3]
val = 3
k = remove(nums, val)
print(k)  
print(nums[:k])  

"""
Output:

[Running] python -u "/config/workspace/practices/ass1Q2.py"
2
[2, 2]
[Done] exited with code=0 in 0.025 seconds

"""

""""
💡 
**Q3.** Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

**Example 1:**
Input: nums = [1,3,5,6], target = 5

Output: 2


 """

def search(nums, target):
    left = 0
    right = len(nums) - 1
    
    while left <= right:
        mid = (left + right) 
        
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    
    return left


nums = [1, 3, 5, 6]
target = 5
index = search(nums, target)
print(index)  
  

"""
Output:
write an algorithm with O(log n) runtime complexity 
--> O(log n)

[Running] python -u "/config/workspace/practices/tempCodeRunnerFile.py"
2

[Done] exited with code=0 in 0.026 seconds

"""

""""
💡 
💡 **Q4.** You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.

**Example 1:**
Input: digits = [1,2,3]
Output: [1,2,4]

**Explanation:** The array represents the integer 123.

Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].


"""

def Add(digit):
    n = len(digit)
    
    for i in range(n - 1, -1, -1):
        
        digit[i] += 1
       
        if digit[i] < 10:
            return digit
        
        digit[i] = 0

    digit.insert(0, 1)
    
    return digit


digit = [1, 2, 3]
result = Add(digit)
print(result)  


"""
Output:
[Running] python -u "/config/workspace/practices/ass1Q4.py"
[1, 2, 4]

[Done] exited with code=0 in 0.03 seconds

"""

""""
💡 
💡💡 **Q5.** You are given two integer arrays num1 and num2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in num1 and num2 respectively.

Merge num1 and num2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array num1. To accommodate this, num1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. num2 has a length of n.

**Example 1:**
Input: num1 = [1,2,3,0,0,0], m = 3, num2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]

**Explanation:** The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from num1.


"""

def merge(num1, m, num2, n):
    i = m - 1  
    j = n - 1  
    k = m + n - 1  

    
    while i >= 0 and j >= 0:
        if num1[i] >= num2[j]:
            num1[k] = num1[i]
            i -= 1
        else:
            num1[k] = num2[j]
            j -= 1
        k -= 1

    
    while j >= 0:
        num1[k] = num2[j]
        j -= 1
        k -= 1


num1 = [1, 2, 3, 0, 0, 0]
m = 3
num2 = [2, 5, 6]
n = 3
merge(num1, m, num2, n)
print(num1)  


"""
Output:
[Running] python -u "/config/workspace/practices/ass1Q5.py"
[1, 2, 2, 3, 5, 6]

[Done] exited with code=0 in 0.026 seconds

"""
""""
💡 
💡💡  **Q6.** Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

**Example 1:**
Input: nums = [1,2,3,1]

Output: true


"""

def array(nums):
    s = set()

    for num in nums:
        if num in s:
            return True
        s.add(num)

    return False


nums = [1, 2, 3, 1]
result = array(nums)
print(result)  


"""
Output:
[Running] python -u "/config/workspace/practices/ass1Q6.py"
True

[Done] exited with code=0 in 0.028 seconds

"""
""""
💡 
**Q7.** Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the nonzero elements.

Note that you must do this in-place without making a copy of the array.

**Example 1:**
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]


"""

def move(nums):
    left = 0
    right = 0

    while right < len(nums):
        if nums[right] != 0:
            nums[left] = nums[right]
            left += 1
        right += 1

    while left < len(nums):
        nums[left] = 0
        left += 1


nums = [0, 1, 0, 3, 12]
move(nums)
print(nums)  



"""
Output:
[Running] python -u "/config/workspace/practices/ass1Q7.py"
[1, 3, 12, 0, 0]

[Done] exited with code=0 in 0.027 seconds

"""

""""
💡 
**Q8.** You have a set of integers s, which originally contains all the numbers from 1 to n. Unfortunately, due to some error, one of the numbers in s got duplicated to another number in the set, which results in repetition of one number and loss of another number.

You are given an integer array nums representing the data status of this set after the error.

Find the number that occurs twice and the number that is missing and return them in the form of an array.

**Example 1:**
Input: nums = [1,2,2,4]
Output: [2,3]


"""

def findnums(nums):
    s = set()
    duplicate = None
    missing = None
    
    for num in nums:
        if num in s:
            duplicate = num
        s.add(num)
    
    for i in range(1, len(nums) + 1):
        if i not in s:
            missing = i
    
    return [duplicate, missing]


nums = [1, 2, 2, 4]
result = findnums(nums)
print(result)  


"""
Output:
[Running] python -u "/config/workspace/practices/ass1Q8.py"
[2, 3]

[Done] exited with code=0 in 0.025 seconds

"""