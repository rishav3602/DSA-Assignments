"""
<aside>
💡 **Question 1**

Given an integer `n`, return *`true` if it is a power of three. Otherwise, return `false`*.

An integer `n` is a power of three, if there exists an integer `x` such that `n == 3x`.

**Example 1:**

```
Input: n = 27
Output: true
Explanation: 27 = 33
```

**Example 2:**

```
Input: n = 0
Output: false
Explanation: There is no x where 3x = 0.

```

**Example 3:**

```
Input: n = -1
Output: false
Explanation: There is no x where 3x = (-1).
```

</aside>
"""

def isPowerOfThree(n):
    while n > 1:
        if n % 3 != 0:
            return False
        n /= 3
    return n == 1



"""
<aside>
💡 **Question 2**

You have a list `arr` of all integers in the range `[1, n]` sorted in a strictly increasing order. Apply the following algorithm on `arr`:

- Starting from left to right, remove the first number and every other number afterward until you reach the end of the list.
- Repeat the previous step again, but this time from right to left, remove the rightmost number and every other number from the remaining numbers.
- Keep repeating the steps again, alternating left to right and right to left, until a single number remains.

Given the integer `n`, return *the last number that remains in* `arr`.

**Example 1:**

```
Input: n = 9
Output: 6
Explanation:
arr = [1, 2,3, 4,5, 6,7, 8,9]
arr = [2,4, 6,8]
arr = [2, 6]
arr = [6]

```

**Example 2:**

```
Input: n = 1
Output: 1
```

</aside>
"""

def lastRemaining(n):
    if n == 1:
        return 1
    powerOfTwo = 1
    while powerOfTwo * 2 <= n:
        powerOfTwo *= 2
    if powerOfTwo == n:
        return n
    return 2 * (n - powerOfTwo)



"""
<aside>
💡 **Question 3**

****Given a set represented as a string, write a recursive code to print all subsets of it. The subsets can be printed in any order.

**Example 1:**

Input :  set = “abc”

Output : { “”, “a”, “b”, “c”, “ab”, “ac”, “bc”, “abc”}

**Example 2:**

Input : set = “abcd”

Output : { “”, “a” ,”ab” ,”abc” ,”abcd”, “abd” ,”ac” ,”acd”, “ad” ,”b”, “bc” ,”bcd” ,”bd” ,”c” ,”cd” ,”d” }

</aside>
"""

def generateSubsets(set):
    subsets = []

    def backtrack(subset, index):
        subsets.append(subset)
        for i in range(index, len(set)):
            backtrack(subset + set[i], i + 1)

    backtrack("", 0)
    return subsets



"""
<aside>
💡 **Question 4**

Given a string calculate length of the string using recursion.

**Examples:**

```
Input : str = "abcd"
Output :4

Input : str = "GEEKSFORGEEKS"
Output :13
```

</aside>
"""

def stringLength(str):
    if str == "":
        return 0
    return 1 + stringLength(str[1:])



"""
<aside>
💡 **Question 5**

We are given a string S, we need to find count of all contiguous substrings starting and ending with same character.

**Examples :**

```
Input  : S = "abcab"
Output : 7
There are 15 substrings of "abcab"
a, ab, abc, abca, abcab, b, bc, bca
bcab, c, ca, cab, a, ab, b
Out of the above substrings, there
are 7 substrings : a, abca, b, bcab,
c, a and b.

Input  : S = "aba"
Output : 4
The substrings are a, b, a and aba
```

</aside>
"""

def countSubstrings(S):
    count = 0
    for i in range(len(S)):
        for j in range(i, len(S)):
            if S[i] == S[j]:
                count += 1
    return count



"""
<aside>
💡 **Question 6**

The [tower of Hanoi](https://en.wikipedia.org/wiki/Tower_of_Hanoi) is a famous puzzle where we have three rods and **N** disks. The objective of the puzzle is to move the entire stack to another rod. You are given the number of discs **N**. Initially, these discs are in the rod 1. You need to print all the steps of discs movement so that all the discs reach the 3rd rod. Also, you need to find the total moves.**Note:** The discs are arranged such that the **top disc is numbered 1** and the **bottom-most disc is numbered N**. Also, all the discs have **different sizes** and a bigger disc **cannot** be put on the top of a smaller disc. Refer the provided link to get a better clarity about the puzzle.

**Example 1:**

```
Input:
N = 2
Output:
move disk 1 from rod 1 to rod 2
move disk 2 from rod 1 to rod 3
move disk 1 from rod 2 to rod 3
3
Explanation:For N=2 , steps will be
as follows in the example and total
3 steps will be taken.
```

**Example 2:**

```
Input:
N = 3
Output:
move disk 1 from rod 1 to rod 3
move disk 2 from rod 1 to rod 2
move disk 1 from rod 3 to rod 2
move disk 3 from rod 1 to rod 3
move disk 1 from rod 2 to rod 1
move disk 2 from rod 2 to rod 3
move disk 1 from rod 1 to rod 3
7
Explanation:For N=3 , steps will be
as follows in the example and total
7 steps will be taken.
```

</aside>
"""

def towerOfHanoi(N, source, destination, auxiliary):
    if N == 1:
        print("Move disk 1 from rod", source, "to rod", destination)
        return 1
    count = 0
    count += towerOfHanoi(N - 1, source, auxiliary, destination)
    print("Move disk", N, "from rod", source, "to rod", destination)
    count += 1
    count += towerOfHanoi(N - 1, auxiliary, destination, source)
    return count

N = 3  # Number of disks
source = 1  # Source rod
destination = 3  # Destination rod
auxiliary = 2  # Auxiliary rod

total_moves = towerOfHanoi(N, source, destination, auxiliary)
print("Total moves:", total_moves)



"""
<aside>
💡 **Question 7**

Given a string **str**, the task is to print all the permutations of **str**. A **permutation** is an arrangement of all or part of a set of objects, with regard to the order of the arrangement. For instance, the words ‘bat’ and ‘tab’ represents two distinct permutation (or arrangements) of a similar three letter word.

**Examples:**

> Input: str = “cd”
> 
> 
> **Output:** cd dc
> 
> **Input:** str = “abb”
> 
> **Output:** abb abb bab bba bab bba
> 
</aside>
"""

def generatePermutations(str):
    permutations = []

    def backtrack(string, start, end):
        if start == end:
            permutations.append(string)
        else:
            for i in range(start, end + 1):
                string_list = list(string)
                string_list[start], string_list[i] = string_list[i], string_list[start]
                new_string = ''.join(string_list)
                backtrack(new_string, start + 1, end)
                string_list[start], string_list[i] = string_list[i], string_list[start]  # backtrack

    backtrack(str, 0, len(str) - 1)
    return permutations



"""
<aside>
💡 **Question 8**

Given a string, count total number of consonants in it. A consonant is an English alphabet character that is not vowel (a, e, i, o and u). Examples of constants are b, c, d, f, and g.

**Examples :**

</aside>
"""

def countConsonants(str):
    consonants = set('bcdfghjklmnpqrstvwxyz')
    
    def helper(str):
        if str == '':
            return 0
        elif str[0].lower() in consonants:
            return 1 + helper(str[1:])
        else:
            return helper(str[1:])
    
    return helper(str)
