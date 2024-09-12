from main import add


def test_add():
    """Testing the add function"""
    assert add(2, 2) == 4
    assert add(3, 2) == 5
    print("hello")


def test_add2():
    """testing out add function"""
    assert add(2, 2) == 4
    assert add(3, 2) == 5
    assert add(1, 2) == 3
    print("hello again")


if __name__ == "__main__":
    test_add()
    test_add2()
