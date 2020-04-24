def sort_012(input_list):

    left, mid = 0, 0
    right = len(input_list)-1
    pivot = 1
    # count=0
    while mid <= right:
        # count+=1
        if input_list[mid] < pivot:
            temp=input_list[mid]
            input_list[mid], input_list[left] = input_list[left], temp
            mid+=1
            left+=1
        elif input_list[mid] > pivot:
            temp=input_list[mid]
            input_list[mid], input_list[right] = input_list[right], temp
            right-=1

        else:
            mid+=1
        #print(input_list, left,mid, right)
    # print(count)
    return input_list

def test_function(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")

print("______________________________TEST CASE 1__________________________")
test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])

print("______________________________TEST CASE 2__________________________")
test_function([1,2,0])
test_function([2,1,1,0, 0, 0, 1, 1])


print("______________________________EDGE CASE__________________________")
test_function([0, 0, 0])
test_function([])
