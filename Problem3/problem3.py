def merge_sort(arr):

    #base case
    if len(arr)==1:
        return arr

    mid = (len(arr))//2

    #left
    left = merge_sort(arr[:mid])

    #right
    right = merge_sort(arr[mid:])

    #merge
    return merge(left, right)

def merge(left, right):
    left_index, right_index = 0, 0

    #merged
    merged = []

    #loop
    while left_index < len(left) and right_index < len(right):

        #sort in descending order
        if left[left_index] > right[right_index]:
            merged.append(left[left_index])
            left_index+=1

        else:
            merged.append(right[right_index])
            right_index+=1
    merged+= left[left_index:]
    merged+= right[right_index:]

    return merged

def rearrange_digits(input_list):

    if len(input_list)<2:
        return input_list

    input_list = merge_sort(input_list)
    str1, str2 = "" , ""

    # pattern finding
    for x in range(len(input_list)):
        if x%2==0:
            str1+=str(input_list[x])
        else:
            str2+=str(input_list[x])
    return [int(str1), int(str2)]

def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

print("______________________________TEST CASE 1__________________________")
test_function([[1, 2, 3, 4, 5], [542, 31]])
test_case = [[4, 6, 2, 5, 9, 8], [964, 852]]
test_function(test_case)
print("______________________________TEST CASE 3__________________________")

test_case1 = [[1, 2, 3, 4], [42, 31]]
test_function(test_case1)
test_case2 = [[1, 2, 6, 3, 4], [631, 42]]
test_function(test_case2)

print("______________________________EDGE CASEs__________________________")

edge_case1 = [[],[]]
edge_case2 = [[1], [1]]
test_function(edge_case2)
test_function(edge_case1)
