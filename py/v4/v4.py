import numpy as np
from random import randint
from itertools import repeat


# nth number in mth row of pascal's triangle
# choose(m,n) = m!/n!(m-n)!
def choose(m, n):
    if m<n:
        raise ValueError("ERROR: m<n")
 
    x = 1
    y = 1
    for i in range(m-n+1, m+1):
        x *= i
    
    for j in range(1, n+1):
        y *= j

    return x/y


rows = int(input("Enter number of rows: ") or 10)
MAX = int(input("Enter number of marbles: ") or 1000)


arr = np.zeros(rows+1, dtype=int)


print("Loading marbles...\n")

s = 0
while s<MAX:
    n = sum(randint(0,1) for _ in repeat(None, rows))
    arr[n] += 1
    s += 1

print("Result ", arr)

pascal_x = np.array([choose(rows, n) for n in range(rows+1)])
expected = pascal_x*sum(arr)/2**rows

print("Expected ", expected)


