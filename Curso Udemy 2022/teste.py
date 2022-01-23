def f(var):
    print(var)


def volta():
    return f

var = volta()
print(id(var), (id(f)))