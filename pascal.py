import random,sys,os
d = {}
num = {}
items = []
results = []
r = input("Enter row number: ") or 5

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
    d['c' + str(x)] = 0
    items.append(getitem(row+1, x))

while True:
    try:
        sum = 0
        for a in range(row):
            sum += random.getrandbits(1)
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