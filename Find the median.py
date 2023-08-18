'''
Given an array arr[] of N integers, calculate the median
 

Example 1:

Input: N = 5
arr[] = 90 100 78 89 67
Output: 89
Explanation: After sorting the array 
middle element is the median 

Example 2:

Input: N = 4
arr[] = 56 67 30 79
Output: 61
Explanation: In case of even number of 
elements, average of two middle elements 
is the median.

 

Your Task:
You don't need to read or print anything. Your task is to complete the function find_median() which takes the array as input parameter and returns the floor value of the median.
 

Expected Time Complexity: O(n * log(n))
Expected Space Complexity: O(1)
 

Constraints:
1 <= Length of Array <= 100
1 <= Elements of Array <= 100'''

# User function Template for python3


class Solution:
    def find_median(self, v):
        # Code here
        if len(v) % 2 == 0:
            v.sort()
            return (v[(len(v)-1)//2] + v[(len(v)-1)//2 + 1]) // 2
        else:
            v.sort()
            return (v[len(v) // 2])


# {
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        n = int(input())
        v = list(map(int, input().split()))
        ob = Solution()
        ans = ob.find_median(v)
        print(ans)
# } Driver Code Ends
