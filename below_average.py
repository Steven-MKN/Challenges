def get_below_average(arr: list):
    belows = []
    sum = 0
    for i in arr:
        sum = sum + i
    q2 = sum/len(arr)
    for i in arr:
        if i < q2:
            belows.append(i)
    return belows

print(get_below_average([1,3,7,5,6,3,4,5,8,9,3,3,5,6,3,4,3]))