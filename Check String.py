'''
Given a string, check if all its characters are the same or not.

Example 1:

Input:
s = "geeks"
Output: False
Explanation: The string contains different
character 'g', 'e', 'k' and 's'.

Example 2:

Input: 
s = "gggg"
Output: True
Explanation: The string contains only one
character 'g'.

Your Task:
You don't need to read input or print anything. Your task is to complete the function check() which takes a string as input and returns True if all the characters in the string are the same. Else, it returns False.


Expected Time Complexity: O(|S|).
Expected Auxiliary Space: O(1).


Constraints:
1 <= |S| <= 104
 '''

# User function Template for python3


class Solution:
    def check(self, s):
        # your code here
        result = True

        for i in s:
            if i != s[0]:
                result = False

        return result


# {
 # Driver Code Starts
# Initial Template for Python 3

t = int(input())
for tc in range(t):
    s = input()
    ob = Solution()
    if ob.check(s):
        print("YES")
    else:
        print("NO")

# Contributed By: Pranay Bansal

# } Driver Code Ends
