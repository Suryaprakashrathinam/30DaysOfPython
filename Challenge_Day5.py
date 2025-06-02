def sum(*args):
    total = 0
    for num in args:
        total += num
    return total

def average(*args):
    if len(args) ==0:
        return 0
    return sum(*args)/len(args)

total = sum(1,2,3,4, 5, 84, 49)
avg = round(average(1,2,3,4, 5, 84, 49), 2)

print ("Total: ", total)
print ("Average:", avg)