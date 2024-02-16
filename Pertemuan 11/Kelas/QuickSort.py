def quicksort(data, start, end):
    if start<end:
        pivot_index=partition(data, start, end)
        quicksort(data, start, pivot_index-1)
        quicksort(data, pivot_index+1, end)

def partition(data, start, end):
    pivot=data[end]
    left=start
    right=end-1
    while left<=right:
        while data[left]<pivot:
            left+=1
        while data[right]>pivot:
            right-=1
        if left<=right:
            data[left], data[right]=data[right], data[left]
            left+=1
            right-=1
    data[left], data[end]=data[end], data[left]
    return left

data=[10, 20, 25, 73, 100, 45, 101, 9]
quicksort(data, 0,len(data)-1)
print(data)