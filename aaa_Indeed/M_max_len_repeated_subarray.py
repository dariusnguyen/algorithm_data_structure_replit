'''
718. Maximum Length of Repeated Subarray
Medium

Given two integer arrays nums1 and nums2, return the maximum length of a subarray that appears in both arrays.

Example 1:

Input: nums1 = [1,2,3,2,1], nums2 = [3,2,1,4,7]
Output: 3
Explanation: The repeated subarray with maximum length is [3,2,1].

Example 2:

Input: nums1 = [0,0,0,0,0], nums2 = [0,0,0,0,0]
Output: 5
'''

'''
Subarray => continuous? Y

Constraints?
1 <= nums1.length, nums2.length <= 1000
0 <= nums1[i], nums2[i] <= 100
Time space complexity constraints?
O(m*n)
O(m*n)

Edge cases:
1. Empty array(s)? => return 0

Brute force:
Time: O(m*n*min(m,n))
Space: O( min(m,n) )

DP:
init memo to memoize previous results
populate memo bottom up
if A[i] = B[j]
	maxlen = 1 + maxlen(A[i+1], B[j+1])
need to populate memo for m+1 and n+1 entries

Time: O(m*n)
Space: O(m*n)
'''

def findLength(nums1, nums2):
	'''
	Method 1: use a dictionary as the memo
	The memo dict doesn't need to be prepopulated with 0's
	but then we need an if statement to check if i+1 or j+1 is out of bounds
	'''
	
	memo = {}

	maxLen = 0
	for i in range(len(nums1)-1, -1, -1):
		for j in range(len(nums2)-1, -1, -1):
			if nums1[i] == nums2[j]:
				#if i+1 or j+1 is out of bounds, then we are at the end of one of the arrays. 
				if i+1>len(nums1)-1 or j+1>len(nums2)-1:
					memo[i, j] = 1					
				else:
					memo[i, j] = 1 + memo[i+1, j+1]				 
				maxLen = max(maxLen, memo[i, j])
			else:
				memo[i, j] = 0
	print(memo)
	return maxLen

def findLength2(nums1, nums2):
	'''
	Method 2:
	Also using DP but use an array of size (m+1) * (n+1) to store the memo
	The array is initialized with 0's
	This allows skipping the out of bounds check
	'''
	memo = [[0]*(len(nums1)+1) for _ in range(len(nums2)+1)]
	maxLen = 0
	for i in range(len(nums1)-1, -1, -1):
		for j in range(len(nums2)-1, -1, -1):
			if nums1[i] == nums2[j]:
				memo[i][j] = 1 + memo[i+1][j+1]
				maxLen = max(memo[i][j], maxLen)
	return maxLen
	

'''
Similar problem: URL History

We have some clickstream data that we gathered on our client's website. Using cookies, we collected snippets of users' anonymized URL histories while they browsed the site. The histories are in chronological order, and no URL was visited more than once per person.
Write a function that takes two users' browsing histories as input and returns the longest contiguous sequence of URLs that appears in both.

Sample input:
user0 = ["/start", "/pink", "/register", "/orange", "/red", "a"]
user1 = ["/start", "/green", "/blue", "/pink", "/register", "/orange", "/one/two"]
user2 = ["a", "/one", "/two"]
user3 = ["/pink", "/orange", "/yellow", "/plum", "/blue", "/tan", "/red", "/amber", "/HotRodPink", "/CornflowerBlue", "/LightGoldenRodYellow", "/BritishRacingGreen"]
user4 = ["/pink", "/orange", "/amber", "/BritishRacingGreen", "/plum", "/blue", "/tan", "/red", "/lavender", "/HotRodPink", "/CornflowerBlue", "/LightGoldenRodYellow"]
user5 = ["a"]

Sample output:
findContiguousHistory(user0, user1)
/pink
/register
/orange

findContiguousHistory(user1, user2)
(empty)

findContiguousHistory(user2, user0)
a

findContiguousHistory(user5, user2)
a

findContiguousHistory(user3, user4)
/plum
/blue
/tan
/red

findContiguousHistory(user4, user3)
/plum
/blue
/tan
/red

'''

'''
user0 = ["/start", "/pink", "/register", "/orange", "/red", "a"]
user1 = ["/start", "/green", "/blue", "/pink", "/register", "/orange", "/one/two"]

["/pink", "/register", "/orange"]
len(useri) >= 1
len(useri[i]) >= 1

init memo as array for memoization
    memo has 1 extra row and 1 extra col
    memo is init with []
    
init maxLenSub = []
loop from end to beginning in arr1 
    loop from end to beginning in arr2
        if arr1[i] == arr2[j]
            memo[i][j] = memo[i+1][j+1].append(arr1[i])
            if len(maxLenSub)<len(memo[i][j])
                maxLenSub = memo[i][j]
return maxLenSub

time: O(m*n) where m is the length of arr1, n is the length of arr2
space: O(m*n)
'''

def findContiguousHistory(arr1, arr2):
    memo = [ [[] for _ in range(len(arr2)+1)] for _ in range(len(arr1)+1)]
    # print(len(memo), len(memo[0]))
    # print(memo)
    maxLenSub = []
    
    for i in range(len(arr1)-1, -1, -1):
        for j in range(len(arr2)-1, -1, -1):
            if arr1[i] == arr2[j]:
                memo[i][j] = [arr1[i]] + memo[i+1][j+1]
                if len(maxLenSub) < len(memo[i][j]):
                    maxLenSub = memo[i][j]
    return maxLenSub

