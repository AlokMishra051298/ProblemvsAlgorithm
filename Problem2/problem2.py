def find_pivot(arr):
    # count=0
    start=0
    end=len(arr)-1
    while start <= end:
        # count+=1
        # print(count)
        mid= ( start + end ) // 2
        #if mid+1 is less than mid it means pivot is arr[mid]
        if arr[mid] > arr[mid + 1]:
            return mid+1
        #if start is less than mid, they are is sequence and need to shift start
        if arr[start] <= arr[mid]:
            start=mid+1
        #else need to shift end
        else:
            end=mid-1

def binarySearch(arr, start, end, x):

    while start <= end:

        mid = start + (end - start) // 2

        # Check if x is present at mid
        if arr[mid] == x:
            return mid

        # If x is greater, ignore left half
        elif arr[mid] < x:
            start = mid + 1

        # If x is smaller, ignore right half
        else:
            end = mid - 1

    # If we reach here, then the element
    # was not present
    return -1

def rotated_array_search(arr,value):

    if len(arr)==0:
        return -1
    if len(arr)==1:
        if arr[0]==value:
            return 0
        return -1
    pivot = find_pivot(arr)

    get = binarySearch(arr, 0, pivot-1, value)
    if get == -1:
        get = binarySearch(arr, pivot, len(arr)-1, value)
    return get

def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")

print("______________________________TEST CASE 1__________________________")
test_function([[6, 7, 8, 9, 10, 11, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])

print("______________________________TEST CASE 2__________________________")
test_function([[1, 2, 3, 4,5,6,7,0], 10])
test_function([[-1, -2, -3, -4, 0, 1, 2, 3], 0])


print("______________________________TEST CASE 3__________________________")

test_function([[0, -1], 1]) #edge cases
test_function([[1], 1]) #edge cases
test_function([[], 0]) #edge case
