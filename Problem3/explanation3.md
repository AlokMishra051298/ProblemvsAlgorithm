# Code design

We used merge sort, because we need that is best sort among all.

1. First we make codition for edge cases, .i.e. If the array is or length 0 or 1, we returned input_list.
2. Else, we call merge sort to sort our input_list. After sorting input_list we start finding pattern. And here we used if index value is divide by 2 then, we add it the 1st string else, add it to 2nd string.
3. After iterating over whole input_list, we convert those strings to integer and return as list of numbers.   

# Time complexity
> **O(nlogn) + O(n)** -> O(nlogn) for merge sort and O(n) to iterate over whole list to find out the pattern

> Result is **O(nlogn)**

# Space Complexity
> O(n)
