#User function Template for python3

class Solution:
    def arraySortedOrNot(self, arr, n):
        # code here
        array_size = len(arr)
        for index in range(array_size - 1):
            if arr[index] > arr[index + 1]:
                return False
        
        return True
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        
        ob = Solution()
        ans = ob.arraySortedOrNot(arr, n)
        if ans:
            print(1)
        else:
            print(0)
        tc -= 1

# } Driver Code Ends