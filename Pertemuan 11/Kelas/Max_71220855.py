import math

def max(data, start, end, max_value):
    if start == end:
        max_value=data[start]
        return max_value
    elif start==end-1:
        if data[start]>data[end]:
            max_value = data[start]
            return max_value
        else:
            max_value=data[end]
            return max_value
    else:
        mid=(start+end)//2
        left_max = max(data, start, mid, max_value)
        right_max=max(data, mid+1, end, max_value)
        if left_max>right_max:
            return left_max
        else:
            return right_max

data=list([150, 24, 13, 12, 1,10,140,11])
print(max(data, 0, len(data)-1, -math.inf))