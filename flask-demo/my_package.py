def test_fun(aaa):
    print(aaa)
    return aaa + aaa

if __name__ == "__main__":
    aaa = 123
    print(test_fun(aaa))
    aaa = 222
    print(test_fun(aaa))
    aaa = 333
    print(test_fun(aaa))
