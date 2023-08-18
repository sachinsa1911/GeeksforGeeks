'''
Remove all characters except the numeric characters from an alphanumeric string.

Example 1:

Input: S = "AA1d23cBB4"
Output: 1234
Explanation: Remove all characters
other than numbers
Example 2:

Input: S = "a1b2c3"
Output: 123
Explanation: Remove all characters
other than numbers
Your task:
Your task is to complete the function string() which takes a single string as input and returns the string. You need not take any input or print anything.
 

Expected Time Complexity: O(|S|)
Expected Auxiliary Space: O(1)

Constraints:
1 <= |S| <= 105'''

# User function Template for python3


class Solution:
    def removeCharacters(self, S):
        # code here
        result = ''
        for i in S:
            if i.isdigit():
                result += i
        return result

# {
 # Driver Code Starts
# Initial Template for Python 3


if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        s = input()

        ob = Solution()
        answer = ob.removeCharacters(s)

        print(answer)


# } Driver Code Ends
