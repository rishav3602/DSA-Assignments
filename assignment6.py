"""
<aside>
💡 **Question 1**

A permutation perm of n + 1 integers of all the integers in the range [0, n] can be represented as a string s of length n where:

- s[i] == 'I' if perm[i] < perm[i + 1], and
- s[i] == 'D' if perm[i] > perm[i + 1].

Given a string s, reconstruct the permutation perm and return it. If there are multiple valid permutations perm, return **any of them**.

**Example 1:**

**Input:** s = "IDID"

**Output:**

[0,4,1,3,2]

</aside>
"""

def reconstruct_permutation(s):
    n = len(s)
    perm = []
    low = 0
    high = n

    for ch in s:
        if ch == 'I':
            perm.append(low)
            low += 1
        elif ch == 'D':
            perm.append(high)
            high -= 1

    perm.append(low)  # or perm.append(high)

    return perm


"""
<aside>
💡 **Question 2**

You are given an m x n integer matrix matrix with the following two properties:

- Each row is sorted in non-decreasing order.
- The first integer of each row is greater than the last integer of the previous row.

Given an integer target, return true *if* target *is in* matrix *or* false *otherwise*.

You must write a solution in O(log(m * n)) time complexity.

</aside>

**Input:** matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3

**Output:** true
"""

def search_matrix(matrix, target):
    m = len(matrix)
    n = len(matrix[0])
    left = 0
    right = m * n - 1

    while left <= right:
        mid = (left + right) // 2
        row = mid // n
        col = mid % n
        if matrix[row][col] == target:
            return True
        elif matrix[row][col] < target:
            left = mid + 1
        else:
            right = mid - 1

    return False


"""
<aside>
💡 **Question 3**

Given an array of integers arr, return *true if and only if it is a valid mountain array*.

Recall that arr is a mountain array if and only if:

- arr.length >= 3
- There exists some i with 0 < i < arr.length - 1 such that:
    - arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
    - arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
</aside>

**Example 1:**

**Input:** arr = [2,1]

**Output:**

false
"""

def valid_mountain_array(arr):
    n = len(arr)
    if n < 3:
        return False

    i = 0
    while i + 1 < n and arr[i] < arr[i + 1]:
        i += 1

    if i == 0 or i == n - 1:
        return False

    while i + 1 < n and arr[i] > arr[i + 1]:
        i += 1

    return i == n - 1


"""
<aside>
💡 **Question 4**

Given a binary array nums, return *the maximum length of a contiguous subarray with an equal number of* 0 *and* 1.

**Example 1:**

**Input:** nums = [0,1]

**Output:** 2

**Explanation:**

[0, 1] is the longest contiguous subarray with an equal number of 0 and 1.

</aside>
"""

def find_max_length(nums):
    max_len = 0
    count = 0
    sum_count = {0: -1}

    for i, num in enumerate(nums):
        if num == 0:
            count -= 1
        else:
            count += 1

        if count in sum_count:
            max_len = max(max_len, i - sum_count[count])
        else:
            sum_count[count] = i

    return max_len


"""
<aside>
💡 **Question 5**

The **product sum** of two equal-length arrays a and b is equal to the sum of a[i] * b[i] for all 0 <= i < a.length (**0-indexed**).

- For example, if a = [1,2,3,4] and b = [5,2,3,1], the **product sum** would be 1*5 + 2*2 + 3*3 + 4*1 = 22.

Given two arrays nums1 and nums2 of length n, return *the **minimum product sum** if you are allowed to **rearrange** the **order** of the elements in* nums1.

**Example 1:**

**Input:** nums1 = [5,3,4,2], nums2 = [4,2,2,5]

**Output:** 40

**Explanation:**

We can rearrange nums1 to become [3,5,4,2]. The product sum of [3,5,4,2] and [4,2,2,5] is 3*4 + 5*2 + 4*2 + 2*5 = 40.

</aside>
"""

def min_product_sum(nums1, nums2):
    nums1.sort()
    nums2.sort()
    n = len(nums1)
    min_product_sum = 0

    for i in range(n):
        min_product_sum += nums1[i] * nums2[n - 1 - i]

    return min_product_sum


"""
<aside>
💡 **Question 6**

An integer array original is transformed into a **doubled** array changed by appending **twice the value** of every element in original, and then randomly **shuffling** the resulting array.

Given an array changed, return original *if* changed *is a **doubled** array. If* changed *is not a **doubled** array, return an empty array. The elements in* original *may be returned in **any** order*.

**Example 1:**

**Input:** changed = [1,3,4,2,6,8]

**Output:** [1,3,4]

**Explanation:** One possible original array could be [1,3,4]:

- Twice the value of 1 is 1 * 2 = 2.
- Twice the value of 3 is 3 * 2 = 6.
- Twice the value of 4 is 4 * 2 = 8.

Other original arrays could be [4,3,1] or [3,1,4].

</aside>
"""

def find_original_array(changed):
    changed.sort()
    original = []

    for num in changed:
        if num // 2 in original:
            original.remove(num // 2)
        else:
            return []

    return original



"""
def find_original_array(changed):
    changed.sort()
    original = []

    for num in changed:
        if num // 2 in original:
            original.remove(num // 2)
        else:
            return []

    return original
**Input:** n = 3

**Output:** [[1,2,3],[8,9,4],[7,6,5]]
"""

def generate_spiral_matrix(n):
    matrix = [[0] * n for _ in range(n)]
    top, bottom, left, right = 0, n - 1, 0, n - 1
    num = 1

    while True:
        for col in range(left, right + 1):
            matrix[top][col] = num
            num += 1
        top += 1

        if num > n * n:
            break

        for row in range(top, bottom + 1):
            matrix[row][right] = num
            num += 1
        right -= 1

        if num > n * n:
            break

        for col in range(right, left - 1, -1):
            matrix[bottom][col] = num
            num += 1
        bottom -= 1

        if num > n * n:
            break

        for row in range(bottom, top - 1, -1):
            matrix[row][left] = num
            num += 1
        left += 1

        if num > n * n:
            break

    return matrix

"""
<aside>
💡 **Question 8**

Given two [sparse matrices](https://en.wikipedia.org/wiki/Sparse_matrix) mat1 of size m x k and mat2 of size k x n, return the result of mat1 x mat2. You may assume that multiplication is always possible.
**Input:** mat1 = [[1,0,0],[-1,0,3]], mat2 = [[7,0,0],[0,0,0],[0,0,1]]

**Output:**

[[7,0,0],[-7,0,3]]

</aside>
"""

def multiply_sparse_matrices(mat1, mat2):
    m, k, n = len(mat1), len(mat1[0]), len(mat2[0])
    result = {}

    for i in range(m):
        result[i] = {}

        for j in range(n):
            result[i][j] = 0

            for k in range(k):
                if mat1[i][k] != 0 and mat2[k][j] != 0:
                    result[i][j] += mat1[i][k] * mat2[k][j]

    result_matrix = [[result[i][j] for j in range(n)] for i in range(m)]
    return result_matrix

mat1 = [[1, 0, 0], [-1, 0, 3]]
mat2 = [[7, 0, 0], [0, 0, 0], [0, 0, 1]]
result = multiply_sparse_matrices(mat1, mat2)
for row in result:
    print(row)
