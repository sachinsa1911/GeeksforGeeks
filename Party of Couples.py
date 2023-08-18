'''
In a party of N people, each person is denoted by an integer. Couples are represented by the same number. Find out the only single person in the party of couples.


Example 1:

Input: N = 5
arr = {1, 2, 3, 2, 1}
Output: 3
Explaination: Only the number 3 is single.

Example 2:

Input: N = 11
arr = {1, 2, 3, 5, 3, 2, 1, 4, 5, 6, 6}
Output: 4
Explaination: 4 is the only single.

Your Task:
You do not need to read input or print anything. Your task is to complete the function findSingle() which takes the size of the array N and the array arr[] as input parameters and returns the only single person.


Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)


Constraints:
1 ≤ N ≤ 104
1 ≤ arr[i] ≤ 106'''

# User function Template for python3


class Solution:
    def findSingle(self, N, arr):
        # code here
        arr1 = []
        arr2 = []

        for i in arr:
            if i not in arr1:
                arr1.append(i)
            else:
                arr2.append(i)

        for j in arr1:
            if j not in arr2:
                return j


# {
 # Driver Code Starts
# Initial Template for Python 3
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        arr = input().split()
        for itr in range(N):
            arr[itr] = int(arr[itr])

        ob = Solution()
        print(ob.findSingle(N, arr))

# } Driver Code Ends
