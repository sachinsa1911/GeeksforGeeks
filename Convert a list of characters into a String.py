'''
Given a list of characters, merge all of them into a string.

Example 1:

Input:
N = 13
Char array = g e e k s f o r g e e k s
Output: geeksforgeeks 
Explanation: combined all the characters
to form a single string.

Example 2:

Input:
N = 4
Char array = e e b a
Output: eeba
Explanation: combined all the characters
to form a single string.


Your Task:
You dont need to read input or print anything. Complete the function chartostr() which accepts a char array arr and its size  N  as parameter and returns a string.
 

Expected Time Complexity: O(N)
Expected Auxiliary Space: O(N)'''

# User function Template for python3


class Solution:
    def chartostr(self, arr, N):
        # code here
        return ''.join(arr)


# {
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())

    for tcs in range(T):
        N = int(input())
        arr = input().split()
        ob = Solution()
        print(ob.chartostr(arr, N))
# } Driver Code Ends
