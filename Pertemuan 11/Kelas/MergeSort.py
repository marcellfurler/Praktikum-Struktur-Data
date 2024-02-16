def merge_sort(data):
    if len(data)>1:
        mid=len(data)//2
        left=data[:mid]
        right=data[mid:]
        merge_sort(left)
        merge_sort(right)
        
    i=0
    j=0
    k=0

    while i<len(left) and j<len(right):
        if left[i]<=right[j]:
            data[k]=left[i]
            i+=1
        else:
            data[k]=right[j]
            j+=1
        k+=1
    while i<len(left):
        data[k]=left[i]
        i+=1
        k+=1

    while j<len(right):
        data[k]=right[j]
        j+=1
        k+=1

data=[10, 20, 25, 73, 100, 45, 101, 9]
merge_sort(data, 0,len(data)-1)
print(data)