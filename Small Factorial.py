'''
Calculate factorial of a given number N.
 

Example 1:

Input: 5
Output: 120
Explanation: 1 * 2 * 3 * 4 * 5 = 120.
 

Your Task:
You don't need to read or print anything. Your task is to complete the function find_fact() which takes n as input parameter and returns factorial of N.
 

Expected Time Complexity: O(N)
Expected Space Complexity: O(1)
 

Constraints:
1 <= N <= 18'''

# User function Template for python3


class Solution:
    def find_fact(self, n):
        # Code here
        if n == 0 or n == 1:
            return 1
        else:
            return n * self.find_fact(n-1)


# {
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        n = int(input())
        ob = Solution()
        ans = ob.find_fact(n)
        print(ans)

# } Driver Code Ends
