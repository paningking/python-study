a=[1,2,3]
def foo(v):
    v[1]=4
    return v
print(foo(a))
print(a)