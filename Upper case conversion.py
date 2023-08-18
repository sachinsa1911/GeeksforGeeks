'''
Given a string str, convert the first letter of each word in the string to uppercase. 

Example 1:

Input:
str = "i love programming"
Output: "I Love Programming"
Explanation:
'I', 'L', 'P' are the first letters of 
the three words.

Your Task:  
You dont need to read input or print anything. Complete the function transform() which takes s as input parameter and returns the transformed string.


Expected Time Complexity: O(N)
Expected Auxiliary Space: O(N) to store resultant string  


Constraints:
1 <= N <= 104
The original string str only consists of lowercase alphabets and spaces to separate words.'''

# User function Template for python3


class Solution:
    def transform(self, s):
        # code here
        return s.title()


# {
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input().strip()
        ob = Solution()
        print(ob.transform(s))
# } Driver Code Ends
