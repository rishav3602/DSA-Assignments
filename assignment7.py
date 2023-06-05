"""
<aside>
💡 **Question 1**

Given two strings s and t, *determine if they are isomorphic*.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

**Example 1:**

**Input:** s = "egg", t = "add"

**Output:** true

</aside>

<aside>
💡 **Question 2**

Given a string num which represents an integer, return true *if* num *is a **strobogrammatic number***.

A **strobogrammatic number** is a number that looks the same when rotated 180 degrees (looked at upside down).

**Example 1:**

**Input:** num = "69"

**Output:**

true

</aside>

<aside>
💡 **Question 3**

Given two non-negative integers, num1 and num2 represented as string, return *the sum of* num1 *and* num2 *as a string*.

You must solve the problem without using any built-in library for handling large integers (such as BigInteger). You must also not convert the inputs to integers directly.

**Example 1:**

**Input:** num1 = "11", num2 = "123"

**Output:**

"134"

</aside>

<aside>
💡 **Question 4**

Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

**Example 1:**

**Input:** s = "Let's take LeetCode contest"

**Output:** "s'teL ekat edoCteeL tsetnoc"

</aside>

<aside>
💡 **Question 5**

Given a string s and an integer k, reverse the first k characters for every 2k characters counting from the start of the string.

If there are fewer than k characters left, reverse all of them. If there are less than 2k but greater than or equal to k characters, then reverse the first k characters and leave the other as original.

**Example 1:**

**Input:** s = "abcdefg", k = 2

**Output:**

"bacdfeg"

</aside>

<aside>
💡 **Question 6**

Given two strings s and goal, return true *if and only if* s *can become* goal *after some number of **shifts** on* s.

A **shift** on s consists of moving the leftmost character of s to the rightmost position.

- For example, if s = "abcde", then it will be "bcdea" after one shift.

**Example 1:**

**Input:** s = "abcde", goal = "cdeab"

**Output:**

true

</aside>

<aside>
💡 **Question 7**

Given two strings s and t, return true *if they are equal when both are typed into empty text editors*. '#' means a backspace character.

Note that after backspacing an empty text, the text will continue empty.

**Example 1:**

**Input:** s = "ab#c", t = "ad#c"

**Output:** true

**Explanation:**

Both s and t become "ac".

</aside>

<aside>
💡 **Question 8**

You are given an array coordinates, coordinates[i] = [x, y], where [x, y] represents the coordinate of a point. Check if these points make a straight line in the XY plane.

</aside>
"""


"""
<aside>
💡 **Question 1**

Given two strings s and t, *determine if they are isomorphic*.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

**Example 1:**

**Input:** s = "egg", t = "add"

**Output:** true

</aside>

"""

def is_isomorphic(s, t):
    if len(s) != len(t):
        return False

    char_map = {}
    used_chars = set()

    for i in range(len(s)):
        if s[i] in char_map:
            if char_map[s[i]] != t[i]:
                return False
        else:
            if t[i] in used_chars:
                return False
            char_map[s[i]] = t[i]
            used_chars.add(t[i])

    return True


"""
<aside>
💡 **Question 2**

Given a string num which represents an integer, return true *if* num *is a **strobogrammatic number***.

A **strobogrammatic number** is a number that looks the same when rotated 180 degrees (looked at upside down).

**Example 1:**

**Input:** num = "69"

**Output:**

true

</aside>
"""

def is_strobogrammatic(num):
    strobogrammatic_map = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}

    left, right = 0, len(num) - 1
    while left <= right:
        if num[left] not in strobogrammatic_map or strobogrammatic_map[num[left]] != num[right]:
            return False
        left += 1
        right -= 1

    return True

"""

<aside>
💡 **Question 3**

Given two non-negative integers, num1 and num2 represented as string, return *the sum of* num1 *and* num2 *as a string*.

You must solve the problem without using any built-in library for handling large integers (such as BigInteger). You must also not convert the inputs to integers directly.

**Example 1:**

**Input:** num1 = "11", num2 = "123"

**Output:**

"134"

</aside>
"""

def add_strings(num1, num2):
    result = []
    carry = 0
    i, j = len(num1) - 1, len(num2) - 1

    while i >= 0 or j >= 0 or carry:
        n1 = int(num1[i]) if i >= 0 else 0
        n2 = int(num2[j]) if j >= 0 else 0
        current_sum = n1 + n2 + carry
        carry = current_sum // 10
        digit = current_sum % 10
        result.append(str(digit))
        i -= 1
        j -= 1

    return ''.join(result[::-1])

"""
<aside>
💡 **Question 4**

Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

**Example 1:**

**Input:** s = "Let's take LeetCode contest"

**Output:** "s'teL ekat edoCteeL tsetnoc"

</aside>
"""

def reverse_words(s):
    words = s.split()
    reversed_words = [word[::-1] for word in words]
    return ' '.join(reversed_words)


"""
<aside>
💡 **Question 5**

Given a string s and an integer k, reverse the first k characters for every 2k characters counting from the start of the string.

If there are fewer than k characters left, reverse all of them. If there are less than 2k but greater than or equal to k characters, then reverse the first k characters and leave the other as original.

**Example 1:**

**Input:** s = "abcdefg", k = 2

**Output:**

"bacdfeg"

</aside>

"""

def reverse_str(s, k):
    result = ''
    for i in range(0, len(s), 2 * k):
        result += s[i:i + k][::-1] + s[i + k:i + 2 * k]
    return result


"""
<aside>
💡 **Question 6**

Given two strings s and goal, return true *if and only if* s *can become* goal *after some number of **shifts** on* s.

A **shift** on s consists of moving the leftmost character of s to the rightmost position.

- For example, if s = "abcde", then it will be "bcdea" after one shift.

**Example 1:**

**Input:** s = "abcde", goal = "cdeab"

**Output:**

true

</aside>
"""

def rotate_string(s, goal):
    if len(s) != len(goal):
        return False

    return goal in s + s


"""
<aside>
💡 **Question 7**

Given two strings s and t, return true *if they are equal when both are typed into empty text editors*. '#' means a backspace character.

Note that after backspacing an empty text, the text will continue empty.

**Example 1:**

**Input:** s = "ab#c", t = "ad#c"

**Output:** true

**Explanation:**

Both s and t become "ac".

</aside>
"""

def backspace_compare(s, t):
    def process_string(string):
        result = []
        for char in string:
            if char == '#':
                if result:
                    result.pop()
            else:
                result.append(char)
        return ''.join(result)

    return process_string(s) == process_string(t)


"""
<aside>
💡 **Question 8**

You are given an array coordinates, coordinates[i] = [x, y], where [x, y] represents the coordinate of a point. Check if these points make a straight line in the XY plane.

**Example 1:**

![Screenshot 2023-05-29 010117.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/012b0a97-4e4b-49b6-bc95-0531fc712978/Screenshot_2023-05-29_010117.png)



**Input:** coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]

**Output:** true

</aside>
"""

def check_straight_line(coordinates):
    x1, y1 = coordinates[0]
    x2, y2 = coordinates[1]
    if x2 - x1 != 0:
        slope = (y2 - y1) / (x2 - x1)
    else:
        slope = float('inf')
    for i in range(2, len(coordinates)):
        x, y = coordinates[i]
        if x - x1 != 0:
            current_slope = (y - y1) / (x - x1)
        else:
            current_slope = float('inf')
        if current_slope != slope:
            return False
    return True
