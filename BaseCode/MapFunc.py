l = [i for i in range(10)]

def f(x):
    return x * x

r = map(f, l)

print(r)

for i in r:
    print(i)
