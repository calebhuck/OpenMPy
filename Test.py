nonlocal x, y, z

if True == True:
    x = 7
    y = 8
    del x, y

while True:
    for x in range(10):
        assert func() == 1, 2
        break
def func():
    raise Exception
    return 1, 2