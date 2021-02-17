nonlocal x, y, z

try:
    pass
except Exception as e:
    x = 10
except Exception2 as e2:
    y =2
except Exception3 as e3:
    print('blah')
finally:
    print('first finally')

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