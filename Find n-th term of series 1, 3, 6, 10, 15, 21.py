'''
Given a number N, find the Nth term in the series 1, 3, 6, 10, 15, 21…

 

Example 1:

Input :
N = 4 
Output:
10
Explanation:
The 4th term of the Series is 10.
Example 2:

Input :
N = 3 
Output:
6
Explanation:
The 3rd term of the Series is 6.
 

Your Task:
You don't need to read input or print anything. Your task is to complete the function findNthTerm() which takes an Integer N as input and returns the answer.

 

Expected Time Complexity: O(1)
Expected Auxiliary Space: O(1)

 

Constraints:
1 <= N <= 104'''

# User function Template for python3


class Solution:
    def findNthTerm(self, N):
        # code here
        result = (N * (N+1))//2
        return result


# {
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())

        ob = Solution()
        print(ob.findNthTerm(N))
# } Driver Code Ends
