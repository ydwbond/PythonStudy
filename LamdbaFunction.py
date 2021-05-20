def test_fun(fun,x):
    return fun(x)

print(test_fun(lambda x:x+1,10))