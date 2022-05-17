from typing import List, Tuple

# Soring automatically give us O(n log n) in avg and worst case.
# Sliding window technique can optimalize search but after 
#   checking exection time result is quite similar 
# As for now we can skip index() and pop() at the end of function
# that saves a litte bit time 3.9959000000002604e-05 on avg instead of 
# 4.5343999999999246e-05

# Other notes:
#1: adding typing  annotations give more clarity of data flow
#2: after that we do not need a second index and pop


def get_largest_values(numbers: List[int]) -> Tuple[int, int]:
    first = max(numbers)
    i = numbers.index(first)
    numbers.pop(i)
    return first, max(numbers)


import time
st = time.perf_counter()
print(get_largest_values([1,2,3,45,2,3,23]))
print(time.perf_counter() - st)