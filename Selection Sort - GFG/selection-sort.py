#User function Template for python3


class Solution: 
    
    def selectionSort(self, arr, n):
        for i in range(n):
            minn = i
            for j in range(i + 1, n):
                if arr[minn] > arr[j]:
                    minn = j
            arr[i], arr[minn] = arr[minn], arr[i]
        
        return " ".join(str(x) for x in arr)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        Solution().selectionSort(arr, n)
        for i in range(n):
            print(arr[i],end=" ")
        print()
# } Driver Code Ends