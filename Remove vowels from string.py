'''
Given a string, remove the vowels from the string.

Example 1:

Input: S = "welcome to geeksforgeeks"
Output: wlcm t gksfrgks
Explanation: Ignore vowels and print other
characters 
Example 2:

Input: S = "what is your name ?"
Output: wht s yr nm ?
Explanation: Ignore vowels and print other
characters 
Your task:
Your task is to complete the function removeVowels() which takes a single string as input and returns the modified string. You need not take any input or print anything.

Expected Time Complexity: O(|s|)
Expected Auxiliary Space: O(1)

Constraints:
1 <= |S| <= 105
Alphabets are lower cases only

'''

# User function Template for python3


class Solution:
    def removeVowels(self, S):
        # code here
        vowels = 'aeiou'
        result = ''
        for i in S:
            if i not in vowels:
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
        answer = ob.removeVowels(s)

        print(answer)


# } Driver Code Ends
