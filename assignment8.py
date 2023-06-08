"""
<aside>
💡 **Question 1**

Given two strings s1 and s2, return *the lowest **ASCII** sum of deleted characters to make two strings equal*.

**Example 1:**

**Input:** s1 = "sea", s2 = "eat"

**Output:** 231

**Explanation:** Deleting "s" from "sea" adds the ASCII value of "s" (115) to the sum.

Deleting "t" from "eat" adds 116 to the sum.

At the end, both strings are equal, and 115 + 116 = 231 is the minimum sum possible to achieve this.

</aside>
"""

def minimumDeleteSum(s1, s2):
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        dp[i][0] = dp[i - 1][0] + ord(s1[i - 1])

    for j in range(1, n + 1):
        dp[0][j] = dp[0][j - 1] + ord(s2[j - 1])

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(dp[i - 1][j] + ord(s1[i - 1]), dp[i][j - 1] + ord(s2[j - 1]))

    return dp[m][n]

"""
<aside>
💡 **Question 2**

Given a string s containing only three types of characters: '(', ')' and '*', return true *if* s *is **valid***.

The following rules define a **valid** string:

- Any left parenthesis '(' must have a corresponding right parenthesis ')'.
- Any right parenthesis ')' must have a corresponding left parenthesis '('.
- Left parenthesis '(' must go before the corresponding right parenthesis ')'.
- '*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string "".

**Example 1:**

**Input:** s = "()"

**Output:**

true

</aside>
"""

def isValid(s):
    stack = []
    stars = []
    
    for ch in s:
        if ch == '(':
            stack.append(ch)
        elif ch == '*':
            stars.append(ch)
        elif ch == ')':
            if stack:
                stack.pop()
            elif stars:
                stars.pop()
            else:
                return False
    
    while stack and stars:
        if stack[-1] < stars[-1]:
            stack.pop()
            stars.pop()
        else:
            return False
    
    return len(stack) == 0

"""
<aside>
💡 **Question 3**

Given two strings word1 and word2, return *the minimum number of **steps** required to make* word1 *and* word2 *the same*.

In one **step**, you can delete exactly one character in either string.

**Example 1:**

**Input:** word1 = "sea", word2 = "eat"

**Output:** 2

**Explanation:** You need one step to make "sea" to "ea" and another step to make "eat" to "ea".

</aside>
"""

def minSteps(word1, word2):
    m, n = len(word1), len(word2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        dp[i][0] = i

    for j in range(1, n + 1):
        dp[0][j] = j

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + 1

    return dp[m][n]

"""
<aside>
💡 **Question 4**

You need to construct a binary tree from a string consisting of parenthesis and integers.

The whole input represents a binary tree. It contains an integer followed by zero, one or two pairs of parenthesis. The integer represents the root's value and a pair of parenthesis contains a child binary tree with the same structure.
You always start to construct the **left** child node of the parent first if it exists.

</aside>
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def str2tree(s):
    def helper(s, index):
        if index >= len(s):
            return None

        start = index
        while index < len(s) and (s[index].isdigit() or s[index] == '-'):
            index += 1
        val = int(s[start:index])

        node = TreeNode(val)

        if index < len(s) and s[index] == '(':
            index += 1
            node.left, index = helper(s, index)

        if index < len(s) and s[index] == '(':
            index += 1
            node.right, index = helper(s, index)

        while index < len(s) and s[index] != ')':
            index += 1
        index += 1

        return node, index

    if not s:
        return None
    root, _ = helper(s, 0)
    return root


"""
<aside>
💡 **Question 5**

Given an array of characters chars, compress it using the following algorithm:

Begin with an empty string s. For each group of **consecutive repeating characters** in chars:

- If the group's length is 1, append the character to s.
- Otherwise, append the character followed by the group's length.

The compressed string s **should not be returned separately**, but instead, be stored **in the input character array chars**. Note that group lengths that are 10 or longer will be split into multiple characters in chars.

After you are done **modifying the input array,** return *the new length of the array*.

You must write an algorithm that uses only constant extra space.

**Example 1:**

**Input:** chars = ["a","a","b","b","c","c","c"]

**Output:** Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]

**Explanation:**

The groups are "aa", "bb", and "ccc". This compresses to "a2b2c3".

</aside>
"""


def compress(chars):
    n = len(chars)
    anchor = write = 0

    for read in range(n):
        if read + 1 == n or chars[read + 1] != chars[read]:
            chars[write] = chars[anchor]
            write += 1

            if read > anchor:
                count = str(read - anchor + 1)
                for c in count:
                    chars[write] = c
                    write += 1

            anchor = read + 1

    return write


"""
<aside>
💡 **Question 6**

Given two strings s and p, return *an array of all the start indices of* p*'s anagrams in* s. You may return the answer in **any order**.

An **Anagram** is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

**Example 1:**

**Input:** s = "cbaebabacd", p = "abc"

**Output:** [0,6]

**Explanation:**

The substring with start index = 0 is "cba", which is an anagram of "abc".

The substring with start index = 6 is "bac", which is an anagram of "abc".

</aside>
"""

from collections import Counter

def findAnagrams(s, p):
    result = []
    p_counter = Counter(p)
    s_counter = Counter(s[:len(p)-1])

    for i in range(len(p)-1, len(s)):
        s_counter[s[i]] += 1
        if s_counter == p_counter:
            result.append(i - len(p) + 1)
        s_counter[s[i - len(p) + 1]] -= 1
        if s_counter[s[i - len(p) + 1]] == 0:
            del s_counter[s[i - len(p) + 1]]

    return result


"""
<aside>
💡 **Question 7**

Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, etc. Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there will not be input like 3a or 2[4].

The test cases are generated so that the length of the output will never exceed 105.

**Example 1:**

**Input:** s = "3[a]2[bc]"

**Output:** "aaabcbc"

</aside>
"""

def decodeString(s):
    stack = []
    curr_num = 0
    curr_str = ""

    for ch in s:
        if ch.isdigit():
            curr_num = curr_num * 10 + int(ch)
        elif ch == '[':
            stack.append(curr_str)
            stack.append(curr_num)
            curr_str = ""
            curr_num = 0
        elif ch == ']':
            num = stack.pop()
            prev_str = stack.pop()
            curr_str = prev_str + num * curr_str
        else:
            curr_str += ch

    return curr_str


"""
<aside>
💡 **Question 8**

Given two strings s and goal, return true *if you can swap two letters in* s *so the result is equal to* goal*, otherwise, return* false*.*

Swapping letters is defined as taking two indices i and j (0-indexed) such that i != j and swapping the characters at s[i] and s[j].

- For example, swapping at indices 0 and 2 in "abcd" results in "cbad".

**Example 1:**

**Input:** s = "ab", goal = "ba"

**Output:** true

**Explanation:** You can swap s[0] = 'a' and s[1] = 'b' to get "ba", which is equal to goal.

</aside>

"""

def buddyStrings(s, goal):
    if s == goal:
        # Check if there are any repeating characters in s
        return len(set(s)) < len(s)

    if len(s) != len(goal):
        return False

    diff_positions = []
    for i in range(len(s)):
        if s[i] != goal[i]:
            diff_positions.append(i)

    return len(diff_positions) == 2 and s[diff_positions[0]] == goal[diff_positions[1]] and s[diff_positions[1]] == goal[diff_positions[0]]
