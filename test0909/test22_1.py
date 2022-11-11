
def test_a(a, b):
    print(a + b)

def test_b(a, b):
    print(a - b)

print("当前执行方法名为： __name__  = ", __name__)
# print("当前执行方法名为： __main__  = ", __main__)
if __name__ == "__main__":
    test_a(2, 3)