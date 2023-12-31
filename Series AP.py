'''
Given the first 2 terms A1 and A2 of an Arithmetic Series.Find the Nth term of the series. 

Example 1:

Input:
A1=2
A2=3
N=4
Output:
5
Explanation:
The series is 2,3,4,5,6....
Thus,4th term is 5.
Example 2:

Input:
A1=1
A2=2
N=10
Output:
10
Explanation:
The series is1,2,3,4,5,6,7,8,9,10,11..
Thus,10th term is 10.

Your Task:
You don't need to read input or print anything.Your Task is to complete the function nthTermOfAP() which takes three integers A1,A2 and N as input parameters and returns the nth term of the AP that has A1 and A2 as the first and second terms respectively.


Expected Time Complexity:O(1)
Expected Auxillary Space:O(1)


Constraints:
-104<=A1,A2<=104
1<=N<=103
 '''

# User function Template for python3


class Solution:
    def nthTermOfAP(self, A1, A2, N):
        # code here
        diff = A2 - A1
        nth_term = A1 + (N-1) * diff

        return nth_term


# {
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        A1, A2, N = map(int, input().strip().split(' '))
        ob = Solution()
        print(ob.nthTermOfAP(A1, A2, N))
# } Driver Code Ends
