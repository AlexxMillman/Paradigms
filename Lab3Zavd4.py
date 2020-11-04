##True-просте число
##False-складне число
def simple(a):
    i=2
    while a % i != 0:
        i += 1
    return i==a
a = int(input())
print(simple(a))