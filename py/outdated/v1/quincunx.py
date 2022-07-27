import random,sys,os,itertools
d = {}
num = {}
items = []
results = []
r = input("Enter row number: ") or 5

# Getitem function to get the nth item of the mth row in pascal's triangle
def getitem(row, item):
    if item >= row:
        raise ValueError("Error. item should not exceed row")
    elif item > 0:
        multiple = int(row - item) / item
        return int(getitem(row, item - 1) * multiple)
    else:
        return 1

try:
    row = int(r)
    if row < 0:
        raise ValueError
except ValueError:
    print("ValueError")
    
print("Ctrl+C to break")

for x in range(row+1):
    d['c' + str(x)] = 0 # Assign default value 0 to all items
    items.append(getitem(row+1, x)) # Get ratio using function geitem()

while True:
    try:
        sum = 0
        for _ in itertools.repeat(None, row): # Repeat row times
            sum += random.randrange(2) # +0 or 1
        d['c' + str(sum)] += 1
    except KeyboardInterrupt:
        print(':'.join(map(str, items)))
        for x in range(row + 1):
            results.append(d['c' + str(x)])
        print(results)
        break
    except Exception as e:
        print(e)
os.system("pause")
sys.exit(0)
