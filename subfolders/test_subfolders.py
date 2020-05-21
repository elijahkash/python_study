from subfolders import Solution


def test_1():
    assert(Solution.removeSubfolders(None, ["/a", "/a/b", "/c/d", "/c/d/e", "/c/f"]) == ["/a", "/c/d", "/c/f"])


def test_2():
    assert(Solution.removeSubfolders(None, ["/a", "/a/b/c", "/a/b/d"]) == ["/a"])


def test_3():
    assert(Solution.removeSubfolders(None, ["/a/q"]) == ["/a/q"])

# test_3()
