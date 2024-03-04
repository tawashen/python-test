def test_closure(test):
    return test + 1

print (test_closure(1))

test = [test_closure]

print(test[0](2))
