'''
Given two positive integers A and B, find GCD of A and B.


Example 1:

Input: A = 3, B = 6
Output: 3
Explanation: GCD of 3 and 6 is 3

Example 2:

Input: A = 1, B = 1
Output: 1
Explanation: GCD of 1 and 1 is 1

Your Task:  
You don't need to read input or print anything. Complete the function gcd() which takes two positive integers as input parameters and returns an integer.


Expected Time Complexity: O(log(min(A, B)))
Expected Auxiliary Space: O(1)


Constraints:
1 ≤ A, B ≤ 109'''

# User function Template for python3
import math


class Solution:
    def gcd(self, A, B):
        # code here
        return math.gcd(A, B)


# {
 # Driver Code Starts
# Initial Template for Python 3
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        A, B = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.gcd(A, B))
# } Driver Code Ends
