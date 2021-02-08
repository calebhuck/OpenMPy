def square_number(num):
    yield num**2


def func2():
    yield

print('hello world')
y = 0
for x in range(1200):
    y += 1

#pragma omp parallel for num_threads(0)
# comment
for x in range(1200):
    y += 1
    y = square_number(y)

if y == 5:
    pass
