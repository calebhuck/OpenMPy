def dec(*args, **kwargs):
    return


async for x in range(10):
    x = 1 if True else 5
    pass
    break

y = lambda x: x
class test:
    def __init__():
        pass
    pass



nonlocal x, y, z

async with open('file', 'rb') as f, x as p, blah as blah2:
    print('a with stnt')
    blah = 8
    pass

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
async def test():
    pass

def decor1(func):
    def inner():
        x = func()
        return x * x

    return inner

def decor(func):
    def inner():
        x = func()
        return 2 * x

    return inner

@decor1
@decor
async def num():
    return 10

print(num())






