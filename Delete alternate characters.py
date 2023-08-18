'''
Given a string S as input. Delete the characters at odd indices of the string.

Example 1:

Input: S = "Geeks"
Output: "Ges" 
Explanation: Deleted "e" at index 1
and "k" at index 3.
Example 2:

Input: S = "GeeksforGeeks"
Output: "GesoGes"
Explanation: Deleted e, k, f, r, e
k at index 1, 3, 5, 7, 9, 11.

Your Task:  
You dont need to read input or print anything. Complete the function delAlternate() which takes S as input parameter and returns the final string after deletion of characters at odd indices.

Expected Time Complexity: O(|S|)
Expected Auxiliary Space: O(|S|)

Constraints:
1<= |S| <=1000'''

# User function Template for python3


class Solution:
    def delAlternate(ob, S):
        # code here
        arr = list(S)
        result = []
        for i in range(0, len(S)):
            if i % 2 == 0:
                result.append(arr[i])

        return ''.join(result)


# {
 # Driver Code Starts
# Initial Template for Python 3
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        S = input()

        ob = Solution()
        print(ob.delAlternate(S))
# } Driver Code Ends
