'''
Calculate the product of all the elements in an array.

Example 1:

Input:
5
1 2 3 4 5
Output:
120
 

Example 2:

Input:
10
5 5 5 5 5 5 5 5 5 5
Output:
9765625
 

Your Task:  
You don't need to read input or print anything. Your task is to complete the function product() which takes the array Arr[] and its size N as inputs and returns the product of all elements.


Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)

 '''

# {
# Driver Code Starts
# Initial Template for Python 3

# } Driver Code Ends
# User function Template for python3


class Solution:
    def longest(self, arr, n):
        # Code Here
        result = 1
        for i in arr:
            result *= i
        return result


# {
 # Driver Code Starts.


def main():

    T = int(input())

    while (T > 0):
        n = int(input())
        arr = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.longest(arr, n))

        T -= 1


if __name__ == "__main__":
    main()


# } Driver Code Ends
