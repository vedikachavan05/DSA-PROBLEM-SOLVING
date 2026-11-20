def deleteAllOccurrences(arr,X):
    n = len(arr)
    write = 0

    for i in range(n):
        if arr[i] != X:#checking if occurance element w every element i.e x 
            arr[write] = arr[i]#if not then shift left
            write += 1#i for tracking and write for placing value 

    while write < n:
        arr[write] = 0#writing remaining indexes as 0
        write += 1

    return arr