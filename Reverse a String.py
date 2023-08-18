'''
Given a String S , print the reverse of the string as output.

Example 1:

Input: S = "GeeksforGeeks"
Output: "skeeGrofskeeG" 
Explanation: Element at first is at last and
last is at first, second is at second last and 
second last is at second position and so on .
Example 2:

Input: S = "ReversE"
Output: "EsreveR"
Explanation: "E" at first and "R" at last and
"e" at second last and "s" at second and
so on .

Your Task:  
You dont need to read input or print anything. Complete the function revStr() which takes S as input parameter and returns the reversed string .

Expected Time Complexity: O(|S|)
Expected Auxiliary Space: O(|S|)

Constraints:
1<= |S| <=1000'''

# User function Template for python3


class Solution:
    def revStr(ob, S):
        # code here
        return S[::-1]


# {
 # Driver Code Starts
# Initial Template for Python 3
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        S = input()

        ob = Solution()
        print(ob.revStr(S))
# } Driver Code Ends
