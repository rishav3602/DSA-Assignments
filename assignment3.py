"""
**Question 1**
Given an integer array nums of length n and an integer target, find three integers
in nums such that the sum is closest to the target. Return the sum of the three integers.
Answer: To find the sum of three integers in the array nums that is closest to the target,
 you can use a two-pointer approach. Sort the array nums in ascending order, iterate through
   each element, and use two pointers to find the closest sum to the target.


**Question 2**
Given an array nums of n integers, return an array of all the unique quadruplets
[nums[a], nums[b], nums[c], nums[d]] such that:
           ● 0 <= a, b, c, d < n
           ● a, b, c, and d are distinct.
           ● nums[a] + nums[b] + nums[c] + nums[d] == target
Answer: To find unique quadruplets in the array nums whose sum is equal to the target,
 you can use a nested loop approach along with two pointers. Sort the array nums, then
   iterate through the array using two pointers to find the remaining two elements that
     add up to the target minus the first two elements.


**Question 3**
Given an array of integers nums, find the next permutation of nums.
Answer: To find the next lexicographically greater permutation of the given array nums, you can follow these steps:

Starting from the right, find the first pair of adjacent elements (i, i+1) such that nums[i] < nums[i+1].
If such a pair is found, find the smallest element in the subarray nums[i+1:] that is greater 
than nums[i]. Swap these two elements.
Reverse the subarray from index i+1 to the end of the array.
If no such pair is found in step 1, it means the array is already in the highest lexicographical order.
 In this case, reverse the entire array.


**Question 4**
Given a sorted array of distinct integers and a target value, return the index if the target is found.
 If not, return the index where it would be if it were inserted in order.
Answer: To find the index of the target value in the sorted array nums or the index where it should be
 inserted, you can use binary search. Compare the target with the middle element of the array and adjust
   the search range accordingly until the target is found or the search range is exhausted.


**Question 5**
You are given a large integer represented as an integer array digits. Increment the large integer by one
 and return the resulting array of digits.
Answer: To increment the large integer represented by the array digits, you can start from the least
 significant digit and perform the carry operation if necessary. Add 1 to the least significant digit
   and propagate the carry until the most significant digit.


**Question 6**
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
Answer: To find the single element in the array nums that appears only once while others appear twice, you
 can use the XOR operator. XOR all the elements in the array, and the result will be the single element.

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


Answer:- 
def findMissingRanges(nums, lower, upper):
    result = []
    prev = lower - 1

    for i in range(len(nums) + 1):
        curr = nums[i] if i < len(nums) else upper + 1
        if curr - prev >= 2:
            result.append(getRange(prev + 1, curr - 1))
        prev = curr

    return result

def getRange(start, end):
    if start == end:
        return str(start)
    else:
        return str(start) + "->" + str(end)

# Example usage:
nums = [0, 1, 3, 50, 75]
lower = 0
upper = 99
print(findMissingRanges(nums, lower, upper))


Question 8
Given an array of meeting time intervals where intervals[i] = [starti, endi],
determine if a person could attend all meetings.

Example 1:
Input: intervals = [[0,30],[5,10],[15,20]]
Output: false

Answer:- 
def canAttendMeetings(intervals):
    intervals.sort(key=lambda x: x[0])  # Sort intervals by start time

    for i in range(1, len(intervals)):
        if intervals[i][0] < intervals[i - 1][1]:  # Check for overlap
            return False

    return True

# Example usage:
intervals = [[0, 30], [5, 10], [15, 20]]
print(canAttendMeetings(intervals))


"""