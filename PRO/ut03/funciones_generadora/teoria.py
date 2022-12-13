def gen_func(x):
    for i in range(x):
        yield i

a = gen_func(5)

print(a)

for _ in range(3):
    print(next (a))

a = gen_func(5)

print(next(a))