# Code Design
I used three variables left, right and mid.
Pivot = 1 (middle value in 0, 1, 2)

Then we in iterate over input_list we swap in such a way that,
>
    1. if value at mid index is less than pivot it means it cames in left side of mid, so we swap these values and increament the mid and left.
    2. if value at mid index is greater than pivot it means it cames in right side of mid, so we swap it to right and mid values
    & as value at correct place we decrement the right index.
    3. there may a third case when value at mid index is equals to pivot, so we simply decreament the mid value.  

# Time Complexity
> **O(n)**

# Space Completity
> **O(1)** - used no auxilary space
