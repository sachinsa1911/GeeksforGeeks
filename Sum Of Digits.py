'''
Given a number, N. Find the sum of all the digits of N
 

Example 1:

Input:
N = 12
Output:
3
Explanation:
Sum of 12's digits:
1 + 2 = 3
Example 2:

Input:
N = 23
Output
5
Explanation:
Sum of 23's digits:
2 + 3 = 5

Your Task:
You don't need to read input or print anything. Your task is to complete the function sumOfDigits() which takes an integer N as input parameters and returns an integer, total sum of digits of N.


Expected Time Complexity: O(log10N)
Expected Space Complexity: O(1)
 

Constraints:
1<=N<=105'''

# User function Template for python3


class Solution:
    def sumOfDigits(self, N):
        # code here
        str_num = str(N)
        sum = 0

        for i in str_num:
            sum = sum + int(i)

        return sum


# {
 # Driver Code Starts
# Initial Template for Python 3
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())

        ob = Solution()
        print(ob.sumOfDigits(N))
# } Driver Code Ends
