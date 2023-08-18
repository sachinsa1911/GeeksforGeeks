'''
Given a English alphabet c, Write a program to check whether a character is a vowel or not.

 

Example 1:

Input:
c = 'a'
Output:
YES
Explanation:
'a' is a vowel.
 

Example 2:

Input:
c = 'Z'
Output:
NO
Explanation:
'Z' is not a vowel.
 

 

Your Task:

You don't need to read input or print anything. Your task is to complete the function isVowel() which takes a character c and returns 'YES' or 'NO'.

 

Expected Time Complexity: O(1)
Expected Auxiliary Space: O(1)

 

Note: c is either lowercase or uppercase English alphabetic character

Constraints:

c belongs to English Alphabets.'''

# User function Template for python3


class Solution:
    def isVowel(ob, c):
        # code here
        vowels = 'aeiou'
        if c.lower() in vowels:
            return 'YES'
        else:
            return 'NO'


# {
 # Driver Code Starts
# Initial Template for Python 3
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):

        c = input()

        ob = Solution()
        print(ob.isVowel(c))
# } Driver Code Ends
