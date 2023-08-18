'''
Given a string S and two integers L and R. Print the characters in the range L to R of the string.
NOTE: Assume zero based indexing.

Example 1:

Input: 
S = "cdbkdub"
L = 0 , R = 5
Output: "cdbkdu" 
Explanation: Starting from index 0 ('c')
to index 5 ('u').
Example 2:

Input: 
S = "sdiblcsdbud"
L = 3 , R = 7
Output: "blcsd"
Explanation: Starting from index 3 ('b')
to index 7 ('d').

Your Task:  
You dont need to read input or print anything. Complete the function javaSub() which takes S, L, R as input parameter and returns the sting from the range L to R.


Expected Time Complexity: O(|S|)
Expected Auxiliary Space: O(|S|)

Constraints:
1<= |S| <=1000
1 <= L <= 800
1 <= R <= 900'''

# User function Template for python3


class Solution:
    def javaSub(ob, S, L, R):
        # code here
        result = ''
        for i in range(L, R+1):
            result += S[i]
        return result


# {
 # Driver Code Starts
# Initial Template for Python 3

# Initial Template for Python 3
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        S = input()
        L, R = input().split()
        L = int(L)
        R = int(R)

        ob = Solution()
        print(ob.javaSub(S, L, R))
# } Driver Code Ends
