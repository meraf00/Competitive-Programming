def countingSort(arr):
    counter = [0] * 100
    for i in arr:
        counter[i] += 1
        
    return counter
        

if __name__ == '__main__':    

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

    print (result)    
