import sys,random,os,itertools
d = {}
num = {}
items = []
results = []

try:
    r = input("Enter row number: ") or 5
except KeyboardInterrupt:
    sys.exit(1)

# Getitem function to get the nth item of the mth row in pascal's triangle
def getitem(row, item):
    if item >= row:
        raise ValueError("Error. item should not exceed row")
    elif item > 0:
        multiple = (row - item) / item
        return int(getitem(row, item - 1) * multiple)
    else:
        return 1

try:
    row = int(r)
    if row < 0:
        raise ValueError
    if row > sys.getrecursionlimit() - 2:
        raise OverflowError
    if row > 34:
        print("Warning: Row number > 34, can cause inaccurate results")
except ValueError:
    sys.exit(r + " not a positive integer")
except OverflowError:
    sys.exit("Row number >", sys.getrecursionlimit() - 2)
    
    
print("Loading marbles...\nCtrl-C to stop!")

for x in range(row+1):
    d['c' + str(x)] = 0 # Assign default value 0 to all items
    items.append(getitem(row+1, x)) # Get ratio using function getitem()

try:
    while True:
        _sum = 0
        for _ in itertools.repeat(None, row): # Repeat row times
            _sum += random.randrange(2) # plus 0 or 1
        d['c' + str(_sum)] +=1
except KeyboardInterrupt:
    print(':'.join(map(str, items)))
    for x in range(row + 1):
        results.append(d['c' + str(x)])
    print(results)
    print("Total:", str(sum(results)))
except:
    print("Exception occured")
finally:
    os.system("pause")
    sys.exit(0)
