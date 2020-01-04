def calc(mod, x, y):
    def arit(_x, _y):
        return _x if _y == 0 else arit(mod(_x, x, _y), _y - 1)
    return arit(x,y)

def add(x, _, __):
    return x + 1

def sub(x, _, __):
    return x - 1 

def mult(x, y, z):
    return x if z == 1 else x + y

